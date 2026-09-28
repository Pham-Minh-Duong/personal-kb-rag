from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from src.rag_chain import get_rag_chain

app = FastAPI(
    title="Personal Knowledge Base RAG API",
    description="API tra cứu kiến thức cá nhân sử dụng RAG, ChromaDB và Ollama",
    version="1.0.0"
)

class QueryRequest(BaseModel):
    question: str
    model: str = "llama3.2"

class QueryResponse(BaseModel):
    question: str
    answer: str

@app.get("/")
def read_root():
    return {"message": "RAG Service is running successfully!"}

@app.post("/chat", response_model=QueryResponse)
def chat_with_rag(request: QueryRequest):
    try:
        rag_chain = get_rag_chain(model_name=request.model)
        # Chuẩn mới truyền tham số 'input' thay vì 'query'
        response = rag_chain.invoke({"input": request.question})
        return QueryResponse(
            question=request.question,
            answer=response["answer"]
        )
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))