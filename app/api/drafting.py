from fastapi import APIRouter, HTTPException

from app.schemas.drafting import DraftRequest, DraftResponse
from app.services.drafting_services import generate_draft


router = APIRouter(
    prefix="/drafting",
    tags=["AI Drafting"]
)


@router.post("/generate", response_model=DraftResponse)
async def generate_document(req: DraftRequest):

    try:
        result = await generate_draft(
            req.template,
            req.details
        )

        return {"document": result}

    except ValueError as e:

        raise HTTPException(
            status_code=400,
            detail=str(e)
        )

    except Exception as e:

        print("Draft Error:", e)

        raise HTTPException(
            status_code=500,
            detail="Draft generation failed"
        )
