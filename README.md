# 🧠 Personal Knowledge Base RAG Application (Second Brain)

A local, privacy-focused **Personal Knowledge Base (Second Brain)** application built with a **Retrieval-Augmented Generation (RAG)** architecture optimized for Vietnamese and multi-language document processing. The entire system is microservice-architected and containerized using **Docker & Docker Compose**, running **100% locally** with zero external API costs.

---

## 🌟 Key Features
- **Local & Privacy-First:** Powered by **Ollama** (Local LLM) and **ChromaDB** (Local Vector DB) to ensure 100% data privacy for your personal notes and documents.
- **Multi-Format Document Support:** Extracts, chunks, and indexes text seamlessly from `.docx`, `.pdf`, and `.txt` files.
- **Production RESTful API:** Built with **FastAPI**, featuring built-in OpenAPI/Swagger UI documentation for easy testing and integration.
- **Production-Ready Containerization:** Multi-container orchestrations via Docker Compose allow deployment on any platform with a single command.

---

## 🛠️️ Tech Stack & Tools
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
