from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import os

# Import our custom modules
import arxiv_call
import index
import conversation
# Import config to ensure .env is loaded when server starts
import config 

app = FastAPI(title="ArXiv RAG API")

# --- DATA MODELS ---
class IngestRequest(BaseModel):
    query: str
    max_results: int = 2

class ChatRequest(BaseModel):
    question: str
    chat_history: list = []

# --- ENDPOINTS ---

@app.get("/")
def home():
    return {"message": "ArXiv RAG API is running"}

@app.post("/ingest")
def ingest_papers(payload: IngestRequest):
    try:
        # Get paper data (including metadata)
        papers_data, log = arxiv_call.search_and_download(payload.query, payload.max_results)
        
        if papers_data:
            # Index the papers
            index_msg = index.create_vector_db(papers_data)
            return {"status": "success", "log": log + "\n" + index_msg}
        
        return {"status": "failed", "log": log}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/chat")
def chat(payload: ChatRequest):
    try:
        
        chain = conversation.get_conversation_chain()
        
        # Convert list of lists to list of tuples for LangChain
        formatted_history = [tuple(x) for x in payload.chat_history]
        
        response = chain.invoke({
            "question": payload.question,
            "chat_history": formatted_history
        })
        
        return {
            "answer": response["answer"],
            "sources": [doc.metadata for doc in response.get('source_documents', [])]
        }
    except Exception as e:
        # This will catch errors like missing OpenRouter key and show them clearly
        print(f"Server Error: {str(e)}") 
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)