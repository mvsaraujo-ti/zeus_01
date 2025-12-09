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


@app.post("/chat")
async def chat_endpoint(req: ChatRequest):
    text = req.get_text()
    answer = await chat_sync(text)
    return {"answer": answer}


@app.post("/rag")
async def rag_endpoint(req: ChatRequest):
    text = req.get_text()
    answer = await rag_answer(text)
    return answer
