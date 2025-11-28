from app.ollama_client import ask_ollama

# Chat simples – conversa DIRETA com o modelo, sem RAG
async def chat_sync(message: str):
    prompt = f"Você é o assistente Zeus. Responda de forma objetiva.\n\nUsuário: {message}\nAssistente:"
    answer = await ask_ollama(prompt)
    return answer
