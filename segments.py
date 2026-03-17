SEGMENT_DICT = {
    # Envelope segments
    "ISA": {
        "name": "Interchange Control Header",
        "loop": "Envelope",
        "purpose": "Opens the EDI interchange; identifies sender, receiver, and control standards.",
        "key_elements": ["ISA06 (Sender ID)", "ISA08 (Receiver ID)", "ISA13 (Control Number)", "ISA15 (Usage: P/T)"]
    },
    "GS": {
        "name": "Functional Group Header",
        "loop": "Envelope",
        "purpose": "Groups related transaction sets; identifies the transaction type and version.",
        "key_elements": ["GS01 (Functional ID: HC)", "GS02 (Sender Code)", "GS03 (Receiver Code)", "GS06 (Group Control Number)"]
    },
    "ST": {
        "name": "Transaction Set Header",
        "loop": "Envelope",
        "purpose": "Opens a single 837 transaction set.",
        "key_elements": ["ST01 (Transaction Set ID: 837)", "ST02 (Transaction Set Control Number)"]
    },
    # Header segments
    "BHT": {
        "name": "Beginning of Hierarchical Transaction",
        "loop": "Header",
        "purpose": "Defines the purpose and type of the 837 transaction (original, replacement, void).",
        "key_elements": ["BHT03 (Reference ID)", "BHT04 (Date)", "BHT06 (Transaction Type: CH=claim, RP=encounters)"]
    },
    # Name / entity segments
    "NM1": {
        "name": "Individual or Organizational Name",
        "loop": "1000A/B, 2000A/B, 2300, 2400",
        "purpose": "Identifies a person or organization (patient, provider, payer, subscriber).",
        "key_elements": ["NM101 (Entity ID)", "NM102 (Type: 1=Person, 2=Org)", "NM103 (Last/Org Name)", "NM109 (NPI/ID)"]
    },
    # Claim-level segments
    "CLM": {
        "name": "Claim Information",
        "loop": "2300",
        "purpose": "Core claim segment; captures patient account number, total charge, place of service, and claim frequency.",
        "key_elements": ["CLM01 (Patient Account Number)", "CLM02 (Total Charge)", "CLM05 (Place of Service:Facility:Frequency)", "CLM11 (Related Cause Code)"]
    },
    "HI": {
        "name": "Health Care Information Codes (Diagnosis)",
        "loop": "2300",
        "purpose": "Carries ICD-10-CM diagnosis codes for the claim (principal + secondary).",
        "key_elements": ["HI01-1 (Code Qualifier: ABK=ICD-10 Principal)", "HI01-2 (Diagnosis Code)", "HI02–HI12 (Additional Diagnoses)"]
    },
    "DTP": {
        "name": "Date or Time Period",
        "loop": "2300, 2400",
        "purpose": "Specifies dates associated with the claim or service line (date of service, admission, discharge).",
        "key_elements": ["DTP01 (Date Qualifier: 472=Service, 435=Admission)", "DTP02 (Format: D8/RD8)", "DTP03 (Date Value)"]
    },
    "REF": {
        "name": "Reference Identification",
        "loop": "2300, 2400",
        "purpose": "Carries reference numbers such as prior authorization, referral, or claim adjustment IDs.",
        "key_elements": ["REF01 (Reference Qualifier: G1=Prior Auth, 9F=Referral)", "REF02 (Reference Number)"]
    },
    "PWK": {
        "name": "Paperwork",
        "loop": "2300",
        "purpose": "Indicates attached supporting documentation (medical records, operative reports).",
        "key_elements": ["PWK01 (Report Type Code)", "PWK02 (Transmission Code)", "PWK05 (Attachment Control Number)"]
    },
    # Service line segments
    "SV1": {
        "name": "Professional Service",
        "loop": "2400",
        "purpose": "Describes a single professional service line (procedure code, charge, units).",
        "key_elements": ["SV101 (Composite: Qualifier:CPT/HCPCS:Modifier)", "SV102 (Charge Amount)", "SV104 (Units)", "SV107 (Diagnosis Code Pointers)"]
    },
    "SV2": {
        "name": "Institutional Service Line",
        "loop": "2400",
        "purpose": "Describes a single institutional service line used in 837I claims.",
        "key_elements": ["SV201 (Revenue Code)", "SV202 (Composite Procedure Code)", "SV203 (Charge Amount)", "SV205 (Units)"]
    },
    "LX": {
        "name": "Service Line Number",
        "loop": "2400",
        "purpose": "Sequential counter that opens each service line (2400 loop) within a claim.",
        "key_elements": ["LX01 (Assigned Number — increments per service line)"]
    },
}
