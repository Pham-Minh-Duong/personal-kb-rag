# 🧠 Personal Knowledge Base RAG Application (Second Brain)

Ứng dụng Tra cứu & Quản lý Tri thức Cá nhân (Second Brain) xây dựng theo kiến trúc **RAG (Retrieval-Augmented Generation)** tối ưu cho tiếng Việt. Dự án được đóng gói hoàn chỉnh dạng microservices sử dụng **Docker & Docker Compose**, hỗ trợ chạy **Local 100%** không tốn chi phí.

---

## 🌟 Tính năng nổi bật
- **Local Privacy First:** Sử dụng Ollama (LLM Local) và ChromaDB giúp bảo mật toàn bộ dữ liệu ghi chú cá nhân.
- **Tiếng Việt & Đa định dạng:** Hỗ trợ đọc và cắt nhỏ văn bản (Chunking) từ các định dạng `.docx`, `.pdf`, `.txt`.
- **RESTful API:** Đóng gói bằng **FastAPI**, tích hợp sẵn Swagger UI trực quan cho việc test và tích hợp ứng dụng khác.
- **Production-Ready Containerization:** Đóng gói toàn bộ FastAPI App và Vector DB trong cụm Docker Container, giúp khởi chạy trên bất kỳ máy tính nào chỉ với 1 câu lệnh.

---

## 🛠️ Công nghệ & Công cụ sử dụng
- **Môi trường phát triển:** VS Code, Antigravity IDE, Miniconda (Python 3.10)
- **Framework & RAG Core:** FastAPI, LangChain, Sentence-Transformers (`all-MiniLM-L6-v2`)
- **Vector Database:** ChromaDB
- **Local LLM Runner:** Ollama (Model: `llama3.2`)
- **API Testing:** Bruno, Swagger UI, `curl` / `Invoke-RestMethod`
- **Đóng gói & Triển khai:** Docker, Docker Compose

---

## 📂 Cấu trúc dự án

```text
personal-kb-rag/
├── data/                  # Thư mục chứa tài liệu/ghi chú cá nhân (.docx, .pdf, .txt)
├── src/                   # Mã nguồn cốt lõi của RAG
│   ├── __init__.py
│   ├── document_loader.py # Xử lý đọc & cắt nhỏ văn bản (Chunking)
│   ├── vector_db.py       # Khởi tạo & Lưu trữ Vector Embeddings vào ChromaDB
│   └── rag_chain.py       # Luồng trích xuất dữ liệu & Truy vấn Ollama
├── app.py                 # FastAPI Web Server (Endpoints /chat)
├── requirements.txt       # Danh sách thư viện Python
├── Dockerfile             # Multi-stage Docker build cho FastAPI App
├── docker-compose.yml     # Quản lý cụm Container (FastAPI + ChromaDB)
└── README.md              # Hướng dẫn dự án