from pydantic import BaseModel, Field


class DraftRequest(BaseModel):
    template: str = Field(..., example="affidavit")
    details: dict = Field(..., example={
        "name": "Rahul Sharma",
        "address": "Delhi",
        "purpose": "Income proof"
    })


class DraftResponse(BaseModel):
    document: str
