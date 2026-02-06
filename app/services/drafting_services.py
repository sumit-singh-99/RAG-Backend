from app.core.llm import ask_llm
from app.core.prompts import (
    DRAFT_REFINER_SYSTEM,
    build_refiner_prompt,
)

# ================== LEGAL TEMPLATES ==================

TEMPLATES = {

    "affidavit": """
AFFIDAVIT

I, {name}, aged about {age} years,
resident of {address},
do hereby solemnly affirm and state as follows:

1. That I am the deponent of this affidavit.

2. That this affidavit is made for the purpose of {purpose}.

3. That the facts stated above are true to my knowledge.

VERIFICATION

Verified at {place} on {date}
that the contents are true.

DEPONENT
{name}
""",

    "rent_agreement": """
RENT AGREEMENT

This agreement is made on {date}
between {owner} and {tenant}.

Property Address:
{property_address}

Monthly Rent: Rs. {rent}

Duration: {duration}

TERMS:
1. Rent shall be paid before 5th of every month.
2. Tenant shall not sublet.
3. Agreement governed by Indian laws.

OWNER: {owner}
TENANT: {tenant}
""",

    "legal_notice": """
LEGAL NOTICE

To,
{recipient}

Subject: {subject}

Sir/Madam,

Under instructions of my client {sender},
I hereby serve this legal notice.

Facts:
{facts}

You are hereby called upon to comply within {days} days.

Failing which legal action will be initiated.

Advocate
{lawyer}
"""
}


# ================== MAIN SERVICE ==================


async def generate_draft(template: str, details: dict) -> str:

    if template not in TEMPLATES:
        raise ValueError("Unsupported template")

    # Step 1: Fill template
    try:
        raw_draft = TEMPLATES[template].format(**details)
    except KeyError as e:
        raise ValueError(f"Missing field: {e}")

    # Step 2: AI Refinement
    prompt = build_refiner_prompt(raw_draft)

    refined = ask_llm(prompt)

    return refined.strip()
