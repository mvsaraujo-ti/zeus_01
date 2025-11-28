from qdrant_client import QdrantClient

# Qdrant local no Windows
QDRANT_HOST = "localhost"
QDRANT_PORT = 6333

client = QdrantClient(
    host=QDRANT_HOST,
    port=QDRANT_PORT
)

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
