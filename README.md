# ================================

# Nyaya Sahayak - Backend (RAG + Drafting API)

# ================================

This is the backend server for Nyaya Sahayak Legal AI.

It provides:

- RAG-based legal question answering
- AI-powered legal document drafting
- PDF ingestion and vector search
- Response generation using Groq LLM API

Tech Stack:

- FastAPI (API Server)
- ChromaDB (Vector Database)
- Sentence Transformers (Embeddings)
- Groq API (LLM)
- Python 3.10+

---

## PROJECT STRUCTURE

rag_backend/
│
├── app/
│ ├── api/ → API routes
│ ├── core/ → AI + LLM logic
│ ├── schemas/ → Request validation
│ ├── services/ → Business logic
│ ├── database/ → Vector DB config
│ └── main.py → App entry
│
├── data/
│ ├── raw_pdfs/ → Legal PDFs
│ └── vectordb/ → Chroma storage
│
├── scripts/
│ └── ingest_docs.py
│
└── requirements.txt

---

## STEP 1: CLONE PROJECT

git clone <your-repo-url>
cd rag_backend

---

## STEP 2: CREATE VIRTUAL ENVIRONMENT

python -m venv venv

# Activate (Windows)

venv\Scripts\activate

# Activate (Linux/Mac)

source venv/bin/activate

---

## STEP 3: INSTALL DEPENDENCIES

pip install -r requirements.txt

---

## STEP 4: SETUP GROQ API KEY

Create a .env file in project root:

touch .env

Add inside .env:

GROQ_API_KEY=your_groq_api_key_here

Get API key from:
https://console.groq.com/

---

## STEP 5: ADD LEGAL PDF FILES

Copy all law / case PDFs into:

data/raw_pdfs/

Example:

data/raw_pdfs/ipc.pdf
data/raw_pdfs/crpc.pdf
data/raw_pdfs/judgements.pdf

---

## STEP 6: INGEST DOCUMENTS (IMPORTANT)

This converts PDFs → embeddings → vector database.

Run:

python scripts/ingest_docs.py

Expected output:

Processing: ipc.pdf
Chunks: XXXX
Saved XXXX chunks

This step is required only when new PDFs are added.

---

## STEP 7: START BACKEND SERVER

Command To Run Server:

uvicorn app.main:app --reload

Server will start at:

http://127.0.0.1:8000

---

## STEP 8: OPEN API DOCUMENTATION

Open in browser:

http://127.0.0.1:8000/docs

Here you can test all APIs.

---

## AVAILABLE ENDPOINTS

1. RAG CHAT API

POST /ask

Request:
{
"question": "What is Section 420 IPC?"
}

Response:
{
"answer": "Section 420 IPC deals with..."
}

2. DOCUMENT DRAFTING API

POST /drafting/generate

Request:
{
"template": "affidavit",
"details": {
"name": "Rahul Sharma",
"address": "Delhi",
"purpose": "Income proof"
}
}

Response:
{
"document": "AFFIDAVIT..."
}

---

## STEP 9: TEST USING CURL

Test Chat API:

curl -X POST http://127.0.0.1:8000/ask \
-H "Content-Type: application/json" \
-d '{"question":"What is Section 420 IPC?"}'

Test Draft API:

curl -X POST http://127.0.0.1:8000/drafting/generate \
-H "Content-Type: application/json" \
-d '{"template":"affidavit","details":{"name":"Rahul Sharma","address":"Delhi","purpose":"Income proof"}}'

---

## HOW BACKEND WORKS (ARCHITECTURE)

1. PDF INGESTION

PDF → Text → Chunks → Embeddings → ChromaDB

2. RAG QUERY FLOW

User Question
↓
Embedding
↓
Vector Search (ChromaDB)
↓
Relevant Chunks
↓
Groq LLM
↓
Final Answer

3. DOCUMENT DRAFTING FLOW

User Details
↓
Prompt Builder
↓
Groq LLM
↓
Legal Document

---

## LLM CONFIGURATION (GROQ)

We use Groq API for response generation.

Models Example:

- llama3-70b-8192
- mixtral-8x7b-32768

Configured in:

app/core/llm.py

---

## IMPORTANT NOTES

- Always run ingestion before querying
- Do not delete data/vectordb after ingestion
- Keep .env file secret
- Restart server after config changes

---

## PRODUCTION DEPLOYMENT (BASIC)

For production:

1. Disable reload

uvicorn app.main:app --host 0.0.0.0 --port 8000

2. Use process manager (PM2 / Supervisor)

3. Use HTTPS + Reverse Proxy (Nginx)

---

## TROUBLESHOOTING

If count = 0:

→ Re-run ingest_docs.py

If API fails:

→ Check .env file
→ Check GROQ_API_KEY

If imports fail:

→ Run from project root
→ Activate venv

---

## DISCLAIMER

This system generates AI-based legal content.

All outputs must be reviewed by a licensed advocate
before official use.

---

## MAINTAINER

Project: Nyaya Sahayak AI
Author: Sumit Singh
License: Educational / Research Use

================================
END OF README
================================
