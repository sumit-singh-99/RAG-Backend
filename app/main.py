from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.api.routes import router
from app.api.drafting import router as drafting_router





app = FastAPI(title="Legal RAG Engine")


app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


app.include_router(router)
app.include_router(drafting_router)


@app.get("/")
def home():
    return {"status": "Legal RAG Running"}
