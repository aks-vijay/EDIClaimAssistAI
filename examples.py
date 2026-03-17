FEW_SHOT_EXAMPLES = [
    {
        "role": "user",
        "content": "What is the purpose of the 2300 loop in an 837P file?"
    },
    {
        "role": "assistant",
        "content": (
            "**2300 Loop — Claim Information**\n\n"
            "The 2300 loop represents a single professional claim and is the core of the 837P transaction. "
            "It sits under the 2000B (Subscriber) loop and can repeat for each claim submitted.\n\n"
            "**Key segments in the 2300 loop:**\n"
            "- `CLM` — Claim-level data: patient account number, total charge, place of service, claim frequency code\n"
            "- `DTP` — Claim dates (date of service, admission date)\n"
            "- `HI` — Diagnosis codes (ICD-10-CM), including principal and secondary diagnoses\n"
            "- `REF` — Reference identifiers (prior authorization number, referral number)\n"
            "- `NM1` — Additional name segments (referring provider, supervising provider)\n\n"
            "The 2300 loop is followed by one or more 2400 loops (service line detail) for each procedure billed on the claim."
        )
    },
    {
        "role": "user",
        "content": "How do I map the CLM segment to a relational database table?"
    },
    {
        "role": "assistant",
        "content": (
            "**Mapping CLM Segment → `claims` Table**\n\n"
            "The `CLM` segment appears once per 2300 loop and contains claim-level identifiers and attributes.\n\n"
            "**Segment example:**\n"
            "```\n"
            "CLM*1234567890*500.00**11:B:1*Y*A*Y*I~\n"
            "```\n\n"
            "**Element-to-column mapping:**\n"
            "| CLM Element | Position | Target Column          | Description                        |\n"
            "|-------------|----------|------------------------|------------------------------------|\n"
            "| CLM01       | 1        | `patient_account_num`  | Patient control number             |\n"
            "| CLM02       | 2        | `total_charge_amount`  | Total claim charge (decimal)       |\n"
            "| CLM05-1     | 5 (comp) | `place_of_service`     | Facility code (e.g., 11 = Office)  |\n"
            "| CLM05-3     | 5 (comp) | `claim_frequency_code` | 1=Original, 7=Replacement, 8=Void  |\n"
            "| CLM11       | 11       | `related_cause_code`   | Accident/injury indicator          |\n\n"
            "**ETL flow:** Raw EDI → tokenize on `~` (segment delimiter) and `*` (element delimiter) "
            "→ extract CLM elements → load into `claims_staging` → apply transformations → insert into production `claims` table."
        )
    },
    {
        "role": "user",
        "content": "What does a TA1 rejection vs a 999 rejection mean?"
    },
    {
        "role": "assistant",
        "content": (
            "**EDI Acknowledgement Types: TA1 vs 999**\n\n"
            "**TA1 — Interchange Acknowledgement**\n"
            "- Validates the ISA/IEA envelope (outermost wrapper of the EDI file)\n"
            "- A TA1 rejection means the interchange failed before functional groups were processed\n"
            "- Common causes: invalid ISA sender/receiver IDs, malformed ISA date/time, duplicate ISA control number\n\n"
            "**999 — Functional Acknowledgement**\n"
            "- Validates GS/GE functional groups and ST/SE transaction sets\n"
            "- The `AK2` loop identifies the rejected transaction set; `IK3` pinpoints the bad segment and position; `IK4` identifies the bad element\n"
            "- Common error codes: `I6` (invalid group control number), `I10` (segment not in defined transaction set)\n\n"
            "**Troubleshooting order:** Always resolve TA1 errors first — if the ISA envelope is rejected, no 999 will be generated. "
            "Then drill into the 999's `IK3`/`IK4` segments for element-level rejection details."
        )
    }
]
