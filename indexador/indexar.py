import sys, os, zlib

# Corrigir caminho do backend para importar app.*
BACKEND_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "backend"))
sys.path.insert(0, BACKEND_PATH)

from app.embedder import embed_text
from app.qclient import upsert_point

ARTICLES_DIR = "/home/zeus/DEV/Wiki-NHD/articles"


def filename_to_id(filename: str) -> int:
    """Gera um ID numérico único baseado no nome do arquivo."""
    return zlib.crc32(filename.encode("utf-8"))


def index_articles():
    files = [f for f in os.listdir(ARTICLES_DIR) if f.endswith(".md")]
    print("\n🔍 Carregando artigos da Wiki NHD...")
    print(f"📄 {len(files)} artigos encontrados.\n")

    for filename in files:
        path = os.path.join(ARTICLES_DIR, filename)

        with open(path, "r", encoding="utf-8") as file:
            text = file.read()

        print(f"🔎 Indexando: {filename}")

        vector = embed_text(text).tolist()

        payload = {
            "file": filename,
            "text": text
        }

        point_id = filename_to_id(filename)

        upsert_point(
            point_id=point_id,
            vector=vector,
            payload=payload
        )

        print(f"✔️ Indexado: {filename} (ID: {point_id})\n")

    print("🎉 Concluído! Zeus agora usa a Wiki NHD como base de conhecimento.")


if __name__ == "__main__":
    index_articles()
