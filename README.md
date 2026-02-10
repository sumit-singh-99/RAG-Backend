<div align="center">

# 🏛️ Nyaya Sahayak Backend

**AI-Powered Legal Assistant with RAG & Document Drafting**

[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![FastAPI](https://img.shields.io/badge/FastAPI-0.104+-green.svg)](https://fastapi.tiangolo.com/)
[![License](https://img.shields.io/badge/license-Educational-orange.svg)](LICENSE)

[Features](#-features) • [Installation](#-installation) • [API Documentation](#-api-endpoints) • [Architecture](#-architecture) • [Deployment](#-deployment)

</div>

---

## 📋 Overview

**Nyaya Sahayak Backend** is a sophisticated legal AI system that leverages Retrieval-Augmented Generation (RAG) to provide accurate legal information and automated document drafting capabilities. Built for legal professionals, students, and researchers.

### ✨ Features

- **🔍 RAG-based Legal Q&A** - Ask questions about Indian laws and get precise, context-aware answers
- **📝 AI Document Drafting** - Automatically generate legal documents (affidavits, notices, contracts)
- **📚 PDF Knowledge Base** - Ingest and search through legal documents (IPC, CrPC, case law)
- **⚡ Fast Vector Search** - ChromaDB-powered semantic search for instant retrieval
- **🤖 Advanced LLM** - Powered by Groq's high-performance language models
- **🔒 Secure API** - RESTful API with proper validation and error handling

---

## 🛠️ Tech Stack

| Component | Technology |
|-----------|------------|
| **API Framework** | FastAPI |
| **Vector Database** | ChromaDB |
| **Embeddings** | Sentence Transformers |
| **LLM Provider** | Groq API |
| **Language** | Python 3.10+ |
| **Server** | Uvicorn |

---

## 📂 Project Structure

```
RAG-Backend/
│
├── app/
│   ├── api/               # API route handlers
│   ├── core/              # AI & LLM logic
│   ├── schemas/           # Pydantic models for validation
│   ├── services/          # Business logic layer
│   ├── database/          # Vector DB configuration
│   └── main.py            # FastAPI application entry point
│
├── data/
│   ├── raw_pdfs/          # Legal PDF documents
│   └── vectordb/          # ChromaDB persistent storage
│
├── scripts/
│   └── ingest_docs.py     # PDF ingestion script
│
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
└── README.md              # This file
```

---

## 🚀 Installation

### Prerequisites

- Python 3.10 or higher
- pip package manager
- Git
- Groq API key ([Get it here](https://console.groq.com/))

### Step-by-Step Setup

#### 1️⃣ Clone the Repository

```bash
git clone https://github.com/sumit-singh-99/RAG-Backend.git
cd RAG-Backend
```

#### 2️⃣ Create Virtual Environment

**Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```

**Linux/Mac:**
```bash
python -m venv venv
source venv/bin/activate
```

#### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

#### 4️⃣ Configure Environment Variables

Create a `.env` file in the project root:

```bash
touch .env  # Linux/Mac
# Or create manually on Windows
```

Add your Groq API key:

```env
GROQ_API_KEY=your_groq_api_key_here
```

> 💡 **Get your API key:** Visit [https://console.groq.com/](https://console.groq.com/)

#### 5️⃣ Add Legal Documents

Place your PDF files in the `data/raw_pdfs/` directory:

```bash
data/raw_pdfs/
├── ipc.pdf
├── crpc.pdf
├── evidence_act.pdf
└── case_law.pdf
```

#### 6️⃣ Ingest Documents (Critical Step!)

Convert PDFs to embeddings and store in vector database:

```bash
python scripts/ingest_docs.py
```

**Expected Output:**
```
📄 Processing: ipc.pdf
✂️  Generated 1,247 chunks
✅ Saved 1,247 embeddings to ChromaDB
```

> ⚠️ **Important:** Only run this when adding new PDFs. Do not delete `data/vectordb/` after ingestion.

#### 7️⃣ Start the Server

```bash
uvicorn app.main:app --reload
```

**Server will be available at:** `http://127.0.0.1:8000`

#### 8️⃣ Access Interactive API Documentation

Open in your browser:
- **Swagger UI:** [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
- **ReDoc:** [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## 🔌 API Endpoints

### 1. Legal Question Answering (RAG)

**Endpoint:** `POST /ask`

**Request:**
```json
{
  "question": "What is Section 420 of IPC?"
}
```

**Response:**
```json
{
  "answer": "Section 420 of the Indian Penal Code (IPC) deals with cheating and dishonestly inducing delivery of property...",
  "sources": [
    {
      "text": "Relevant excerpt from IPC...",
      "metadata": {
        "source": "ipc.pdf",
        "page": 142
      }
    }
  ]
}
```

**cURL Example:**
```bash
curl -X POST "http://127.0.0.1:8000/ask" \
  -H "Content-Type: application/json" \
  -d '{"question":"What is Section 420 IPC?"}'
```

---

### 2. Document Drafting

**Endpoint:** `POST /drafting/generate`

**Request:**
```json
{
  "template": "affidavit",
  "details": {
    "name": "Rahul Sharma",
    "address": "123 Legal Street, New Delhi - 110001",
    "purpose": "Income proof for loan application"
  }
}
```

**Response:**
```json
{
  "document": "AFFIDAVIT\n\nI, Rahul Sharma, residing at 123 Legal Street...",
  "template_used": "affidavit",
  "generated_at": "2026-02-10T14:30:00Z"
}
```

**cURL Example:**
```bash
curl -X POST "http://127.0.0.1:8000/drafting/generate" \
  -H "Content-Type: application/json" \
  -d '{
    "template": "affidavit",
    "details": {
      "name": "Rahul Sharma",
      "address": "New Delhi",
      "purpose": "Income proof"
    }
  }'
```

---

## 🏗️ Architecture

### RAG Query Flow

```
┌─────────────────┐
│  User Question  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Embedding     │ ← Sentence Transformers
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Vector Search  │ ← ChromaDB
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│ Retrieve Top-K  │
│  Relevant Docs  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Context +     │
│   Question      │
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│   Groq LLM      │ ← llama3-70b-8192
└────────┬────────┘
         │
         ▼
┌─────────────────┐
│  Final Answer   │
└─────────────────┘
```

### Document Drafting Flow

```
User Input → Template Selection → Prompt Construction → Groq LLM → Legal Document
```

### PDF Ingestion Pipeline

```
PDF Files → Text Extraction → Chunking → Embedding Generation → ChromaDB Storage
```

---

## ⚙️ Configuration

### LLM Settings

Edit `app/core/llm.py` to configure:

```python
# Available Groq Models
MODELS = {
    "llama3-70b": "llama3-70b-8192",      # Recommended for legal Q&A
    "mixtral": "mixtral-8x7b-32768",      # Good for document generation
    "llama3-8b": "llama3-8b-8192"         # Faster, lightweight option
}

# Generation Parameters
MAX_TOKENS = 2048
TEMPERATURE = 0.3  # Lower = more deterministic
TOP_P = 0.9
```

### Vector Database Settings

Edit `app/database/vectordb.py`:

```python
CHUNK_SIZE = 500          # Tokens per chunk
CHUNK_OVERLAP = 50        # Overlap between chunks
TOP_K_RESULTS = 5         # Number of chunks to retrieve
EMBEDDING_MODEL = "all-MiniLM-L6-v2"  # Sentence transformer model
```

---

## 🧪 Testing

### Using Python Requests

```python
import requests

# Test RAG endpoint
response = requests.post(
    "http://127.0.0.1:8000/ask",
    json={"question": "What is Section 302 IPC?"}
)
print(response.json())

# Test drafting endpoint
response = requests.post(
    "http://127.0.0.1:8000/drafting/generate",
    json={
        "template": "affidavit",
        "details": {
            "name": "John Doe",
            "address": "Mumbai",
            "purpose": "Address proof"
        }
    }
)
print(response.json())
```

---

## 🚢 Deployment

### Production Server

```bash
# Disable auto-reload and bind to all interfaces
uvicorn app.main:app --host 0.0.0.0 --port 8000 --workers 4
```

### Using Docker (Optional)

Create a `Dockerfile`:

```dockerfile
FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
```

Build and run:

```bash
docker build -t nyaya-sahayak-backend .
docker run -p 8000:8000 --env-file .env nyaya-sahayak-backend
```

### Recommended Production Setup

1. **Process Manager:** Use PM2 or Supervisor
2. **Reverse Proxy:** Nginx or Caddy
3. **HTTPS:** Let's Encrypt SSL certificate
4. **Monitoring:** Prometheus + Grafana
5. **Logging:** Structured logging with ELK stack

---

## 🐛 Troubleshooting

| Issue | Solution |
|-------|----------|
| **Vector DB empty (count=0)** | Re-run `python scripts/ingest_docs.py` |
| **API returns 401/403** | Check `.env` file and verify `GROQ_API_KEY` |
| **Import errors** | Ensure virtual environment is activated and you're in project root |
| **Server won't start** | Check if port 8000 is already in use: `lsof -i :8000` (Mac/Linux) |
| **Slow responses** | Reduce `TOP_K_RESULTS` or use a smaller embedding model |

### Debug Mode

Enable detailed logging:

```bash
uvicorn app.main:app --reload --log-level debug
```

---

## 📊 Performance Metrics

| Metric | Value |
|--------|-------|
| **Average Response Time** | ~1.5-3s |
| **Embedding Generation** | ~50ms per query |
| **Vector Search** | ~100-200ms |
| **LLM Generation** | ~1-2s |
| **Max Concurrent Requests** | 50+ (with 4 workers) |

---

## 🔐 Security Best Practices

- ✅ Never commit `.env` file to version control
- ✅ Use environment variables for sensitive data
- ✅ Implement rate limiting in production
- ✅ Add authentication middleware (JWT/OAuth)
- ✅ Sanitize user inputs
- ✅ Enable CORS only for trusted domains

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## ⚠️ Disclaimer

This system generates AI-based legal content for **educational and research purposes only**. 

**All outputs MUST be reviewed by a licensed legal professional before official use.** The creators assume no liability for legal decisions made based on this system's output.

---

## 📄 License

This project is licensed for **Educational and Research Use**.

For commercial use, please contact the maintainer.

---

## 👨‍💻 Maintainer

**Project:** Nyaya Sahayak AI  
**Author:** Sumit Singh  
**GitHub:** [@sumit-singh-99](https://github.com/sumit-singh-99)  
**Contact:** [Create an issue](https://github.com/sumit-singh-99/RAG-Backend/issues)

---

## 🙏 Acknowledgments

- **FastAPI** - Modern web framework
- **ChromaDB** - Vector database
- **Groq** - Lightning-fast LLM inference
- **Sentence Transformers** - State-of-the-art embeddings

---

<div align="center">

**⭐ If you find this project helpful, please consider giving it a star!**

Made with ❤️ for the legal community

</div>