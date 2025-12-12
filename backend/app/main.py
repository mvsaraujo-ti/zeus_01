from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel

from app.chat import chat_sync
from app.rag import rag_answer

app = FastAPI(title="ZEUS Backend")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Agora aceita: message, question e text
class ChatRequest(BaseModel):
    message: str | None = None
    question: str | None = None
    text: str | None = None

    def get_text(self):
        return self.text or self.message or self.question


@app.get("/health")
def health():
    return {"status": "ok"}


# ============================================
#  CHAT HÍBRIDO: RAG primeiro + LLM depois
# ============================================
@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    text = req.get_text()

    # 1️⃣ Tenta responder usando a base de conhecimento (RAG)
    rag_result = await rag_answer(text)

    # Se o RAG encontrou resposta relevante → usa ela
    if rag_result and isinstance(rag_result, dict) and rag_result.get("answer"):
        return {"answer": rag_result["answer"]}

    # 2️⃣ Caso contrário, usa o modelo LLM (Llama 3.2)
    llm_answer = await chat_sync(text)
    return {"answer": llm_answer}


# ============================================
#  RAG DIRETO (caso queira testar manualmente)
# ============================================
@app.post("/rag")
async def rag_endpoint(req: ChatRequest):
    text = req.get_text()
    answer = await rag_answer(text)
    return answer
