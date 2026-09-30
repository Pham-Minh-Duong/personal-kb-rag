# 🧠 Personal Knowledge Base RAG Application (Second Brain)

A local, privacy-focused **Personal Knowledge Base (Second Brain)** application built with a **Retrieval-Augmented Generation (RAG)** architecture optimized for Vietnamese and multi-language document processing. The entire system is microservice-architected and containerized using **Docker & Docker Compose**, running **100% locally** with zero external API costs.

---

## 🌟 Key Features

- **Local & Privacy-First:** Powered by **Ollama** (Local LLM) and **ChromaDB** (Local Vector DB) to ensure 100% data privacy for your personal notes and documents.
- **Multi-Format Document Support:** Extracts, chunks, and indexes text seamlessly from `.docx`, `.pdf`, and `.txt` files.
- **Production RESTful API:** Built with **FastAPI**, featuring built-in OpenAPI/Swagger UI documentation for easy testing and integration.
- **Production-Ready Containerization:** Multi-container orchestrations via Docker Compose allow deployment on any platform with a single command.

---

## 🛠 Tech Stack & Tools

- **Development Environment:** VS Code / Cursor / Antigravity IDE, Miniconda (Python 3.10)
- **Frameworks & RAG Engine:** FastAPI, LangChain, HuggingFace Sentence-Transformers (`all-MiniLM-L6-v2` / `paraphrase-multilingual-MiniLM-L12-v2`)
- **Vector Database:** ChromaDB
- **Local LLM Runner:** Ollama (Model: `llama3.2`)
- **API Testing:** Bruno, Swagger UI, `curl` / PowerShell `Invoke-RestMethod`
- **Containerization & Orchestration:** Docker, Docker Compose

---

## 📂 Project Directory Structure

```text
personal-kb-rag/
├── data/                  # Directory for personal documents (.docx, .pdf, .txt)
├── src/                   # Core RAG source code
│   ├── __init__.py        # Package initializer
│   ├── document_loader.py # Document loading & chunking logic
│   ├── vector_db.py       # ChromaDB initialization & vector embedding pipeline
│   └── rag_chain.py       # Retrieval chain & Ollama LLM integration
├── app.py                 # FastAPI application entry point (/chat endpoint)
├── requirements.txt       # Python dependencies
├── Dockerfile             # Container image definition for FastAPI app
├── docker-compose.yml     # Multi-container orchestration (FastAPI + ChromaDB)
├── .gitignore             # Git ignore file for temporary & generated files
└── README.md              # Project documentation
```

---

## 🚀 Quickstart Guide

### 1. Prerequisites

- **Docker Desktop** installed and running.
- **Ollama** installed locally with the `llama3.2` model downloaded:

```bash
ollama pull llama3.2
```

### 2. Launch with Docker Compose (3 Steps)

**Step 1: Clone the Repository**

```bash
git clone [https://github.com/](https://github.com/)<your-username>/personal-kb-rag.git
cd personal-kb-rag
```

**Step 2: Start the Container Stack**

Build and start the services in detached mode:

```bash
docker compose up -d --build
```

*(This builds the FastAPI application image and connects it with the persistent ChromaDB container).*

**Step 3: Ingest Personal Documents into Vector DB**

Add your target documents (`.docx`, `.pdf`, `.txt`) into the `./data/` folder, then execute the vector ingestion script inside the application container:

```bash
docker exec -it fastapi_rag_app python -m src.vector_db
```

---

## 🧪 API Verification & Testing

### Option 1: Interactive Swagger UI

Open your browser and navigate to:
👉 `http://localhost:8001/docs`

### Option 2: PowerShell (Invoke-RestMethod)

```powershell
Invoke-RestMethod -Uri "http://localhost:8001/chat" `
    -Method Post `
    -ContentType "application/json" `
    -Body '{"question": "What technologies are mentioned in my documents?", "model": "llama3.2"}'
```

### Option 3: cURL

```bash
curl -X POST "http://localhost:8001/chat" \
     -H "Content-Type: application/json" \
     -d '{"question": "What technologies are mentioned in my documents?", "model": "llama3.2"}'
```

---

## 👨‍💻 Author

- **Developer:** Duong
- **Project:** Building an End-to-End RAG Application from Zero to Production
