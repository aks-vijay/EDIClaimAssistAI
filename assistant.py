import os
from dotenv import load_dotenv
from openai import OpenAI
import gradio as gr

from config import MODEL, SYSTEM_MESSAGE
from segments import SEGMENT_DICT
from examples import FEW_SHOT_EXAMPLES


class EDIClaimAssistAI:

    def __init__(self):
        load_dotenv(override=True)
        self._validate_api_key()
        self.client = OpenAI()

    def _validate_api_key(self):
        api_key = os.getenv("OPENAI_API_KEY")
        if api_key:
            print("OpenAI API key loaded successfully.")
        else:
            print("Error: OpenAI API key not found. Please set the OPENAI_API_KEY environment variable.")

    def chat(self, message, history, file=None):
        # Add segment reference
        segment_ref = "\n".join(
            f"- {code}: {info['name']} ({info['loop']}) — {info['purpose']}"
            for code, info in SEGMENT_DICT.items()
        )
        message_with_ref = f"{message}\n\n[EDI Segment Reference]\n{segment_ref}"

        # If a file is uploaded, append its content with instructions
        if file:
            file_content = open(file, "r", encoding="utf-8").read()
            message_with_ref += (
                "\n\n[Uploaded 837 File Analysis]\n"
                "Please analyze this 837 file and provide:\n"
                "1. Total claims (2300 loops)\n"
                "2. Total service lines (2400 loops)\n"
                "3. Missing critical segments (CLM, NM1, SV1)\n"
                "4. Duplicate CLM01 values\n\n"
                "Return the results in a table format with columns: Loop | Segment | Issue/Warning | Details\n\n"
                f"File Content:\n{file_content}"
            )

        # Prepare messages for the OpenAI chat
        messages = [{"role": "system", "content": SYSTEM_MESSAGE}]
        messages += FEW_SHOT_EXAMPLES
        messages += [{"role": h["role"], "content": h["content"]} for h in history]
        messages.append({"role": "user", "content": message_with_ref})

        # Call OpenAI API
        response = self.client.chat.completions.create(
            model=MODEL,
            messages=messages
        )
        return response.choices[0].message.content

    def launch(self):
        gr.ChatInterface(
            fn=self.chat,
            additional_inputs=[gr.File(label="Upload EDI 837 File (.txt / .edi)")],
            title="EDIClaimAssist AI",
            description="Ask questions about EDI 837 claims or upload an EDI file for analysis."
        ).launch()

    
