import httpx

OLLAMA_URL = "http://localhost:11434"
MODEL_NAME = "llama3.2"

async def ask_ollama(prompt: str) -> str:
    async with httpx.AsyncClient(timeout=120.0) as client:
        response = await client.post(
            f"{OLLAMA_URL}/api/generate",
            json={
                "model": MODEL_NAME,
                "prompt": prompt,
                "stream": False   # <-- AQUI ESTÁ A SOLUÇÃO
            }
        )

    data = response.json()

    return data.get("response", "")
