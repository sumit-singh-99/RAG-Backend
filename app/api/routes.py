from fastapi import APIRouter
from pydantic import BaseModel

from app.core.rag_engine import rag_answer


router = APIRouter()


class Query(BaseModel):
    question: str


@router.post("/ask")
def ask(query: Query):

    answer = rag_answer(query.question)

    return {
        "question": query.question,
        "answer": answer
    }
