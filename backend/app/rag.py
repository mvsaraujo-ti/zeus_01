import numpy as np
from app.embedder import embed_text
from app.qclient import search
from app.ollama_client import ask_ollama


async def rag_answer(query: str):
    # Gerar embedding da pergunta
    query_vector = embed_text(query).tolist()

    # Buscar APENAS o documento mais relevante (mais rápido e preciso)
    results = search(query_vector, limit=1)

    if not results:
        return {
            "answer": "Nenhuma informação encontrada na base de conhecimento.",
            "sources": []
        }

    # Pegar apenas o documento principal
    top = results[0]
    payload = top.get("payload", {})
    context = payload.get("text", "")

    # Prompt rígido, anti-alucinação e anti-erro
    full_prompt = f"""
Você é o assistente Zeus do TJMA.

Responda SOMENTE com base no CONTEXTO fornecido.
Se a resposta não estiver claramente no contexto, diga exatamente:
"Nenhuma informação encontrada na base de conhecimento."

Regras importantes:
- NÃO assuma nada que não esteja escrito no contexto.
- NÃO invente nomes, passos ou processos.
- Diferencie "solicitar acesso" de "ter acesso".
- Seja direto, objetivo e profissional.

### CONTEXTO ###
{context}

### PERGUNTA ###
{query}

### RESPOSTA ###
"""

    answer = await ask_ollama(full_prompt)

    return {
        "answer": answer.strip(),
        "sources": [top]
    }
