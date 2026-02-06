import chromadb
from chromadb.config import Settings
import os

# Absolute project root
PROJECT_ROOT = os.path.abspath(
    os.path.join(os.path.dirname(__file__), "..", "..")
)

DB_PATH = os.path.join(PROJECT_ROOT, "data", "vectordb")

print("✅ DB PATH:", DB_PATH)


client = chromadb.Client(
    Settings(
        persist_directory=DB_PATH,
        is_persistent=True,
        anonymized_telemetry=False
    )
)

collection = client.get_or_create_collection("legal_docs")
