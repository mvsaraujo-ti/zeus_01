import os
import uuid
from sentence_transformers import SentenceTransformer
from qdrant_client import QdrantClient
from qdrant_client.models import VectorParams, Distance

COLLECTION = "zeus_knowledge"
ARTICLES_DIR = "D:/IA-ZEUS/Zeus.00/articles"

embedder = SentenceTransformer("all-MiniLM-L6-v2")

qdrant = QdrantClient(host="localhost", port=6333)

# Criar coleção se não existir
if not qdrant.collection_exists(COLLECTION):
    qdrant.create_collection(
        collection_name=COLLECTION,
        vectors_config=VectorParams(size=384, distance=Distance.COSINE)
    )

def index_articles():
    files = os.listdir(ARTICLES_DIR)

    for filename in files:
        if not filename.endswith(".md"):
            continue

        path = os.path.join(ARTICLES_DIR, filename)

        with open(path, "r", encoding="utf-8") as f:
            text = f.read()

        vector = embedder.encode(text).tolist()
        doc_id = str(uuid.uuid4())

        qdrant.upsert(
            collection_name=COLLECTION,
            points=[{
                "id": doc_id,
                "vector": vector,
                "payload": {"text": text, "file": filename}
            }]
        )

    print("Indexação concluída!")

if __name__ == "__main__":
    index_articles()
