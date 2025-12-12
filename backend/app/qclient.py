from qdrant_client import QdrantClient
from qdrant_client.http import models as rest

# Qdrant local no Linux
QDRANT_HOST = "localhost"
QDRANT_PORT = 6333

client = QdrantClient(
    host=QDRANT_HOST,
    port=QDRANT_PORT
)


# -----------------------------
# 🔍 BUSCA VETORIAL
# -----------------------------
def search(vector, limit=3):
    response = client.query_points(
        collection_name="zeus_knowledge",
        query=vector,
        limit=limit
    )

    results = []
    for point in response.points:
        results.append({
            "id": point.id,
            "score": point.score,
            "payload": point.payload
        })

    return results


# -----------------------------
# 🧩 INSERIR / ATUALIZAR DOCUMENTO
# -----------------------------
def upsert_point(point_id, vector, payload):

    client.upsert(
        collection_name="zeus_knowledge",
        points=[
            rest.PointStruct(
                id=point_id,
                vector=vector,
                payload=payload
            )
        ]
    )
