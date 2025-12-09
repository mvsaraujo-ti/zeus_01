import os
import uuid
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

COLLECTION = "zeus_knowledge"
ARTICLES_DIR = r"D:\IA-ZEUS\Zeus.00\articles"

embedder = SentenceTransformer("all-MiniLM-L6-v2")
qdrant = QdrantClient(host="localhost", port=6333)

# 🔥 limpar coleção ANTES de indexar
if qdrant.collection_exists(COLLECTION):
    print("Apagando coleção antiga...")
    qdrant.delete_collection(COLLECTION)

qdrant.create_collection(
    collection_name=COLLECTION,
    vectors_config=VectorParams(size=384, distance=Distance.COSINE)
)

def index_articles():
    files = os.listdir(ARTICLES_DIR)

    for filename in files:
        if not filename.lower().endswith((".md", ".txt")):
            continue

        path = os.path.join(ARTICLES_DIR, filename)

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        try:
            vector = embedder.encode(text).tolist()
        except Exception as e:
            print(f"ERRO ao processar {filename}: {e}")
            continue

        doc_id = str(uuid.uuid4())

        qdrant.upsert(
            collection_name=COLLECTION,
            points=[{
                "id": doc_id,
                "vector": vector,
                "payload": {"text": text, "file": filename}
            }]
        )

        print(f"Indexado: {filename}")

    print("Indexação concluída! 🚀")

if __name__ == "__main__":
    index_articles()
