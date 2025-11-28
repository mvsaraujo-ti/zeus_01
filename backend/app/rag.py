import numpy as np
from app.embedder import embed_text
from app.qclient import search
from app.ollama_client import ask_ollama

async def rag_answer(query: str):
    # Gerar embedding da pergunta
    query_vector = embed_text(query).tolist()

    # Buscar os 3 artigos mais relevantes
    results = search(query_vector, limit=3)

    # Construir contexto com os textos recuperados
    context_parts = []
    for item in results:
        payload = item.get("payload", {})
        text = payload.get("text", "")
        context_parts.append(text)

    context = "\n\n---\n\n".join(context_parts)

    # Criar prompt completo
    full_prompt = f"""
Você é o assistente Zeus. Use APENAS as informações abaixo para responder:

### CONTEXTO ###
{context}

### PERGUNTA ###
{query}

Responda de maneira objetiva.
"""

    answer = await ask_ollama(full_prompt)
    return {
        "answer": answer,
        "sources": results
    }
