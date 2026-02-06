import uuid
from app.database.vectordb import collection
from app.core.embeddings import embed_texts


def index_documents(chunks, source):

    embeddings = embed_texts(chunks)

    ids = [str(uuid.uuid4()) for _ in chunks]

    metadatas = [{"source": source} for _ in chunks]

    collection.add(
        documents=chunks,
        embeddings=embeddings,
        ids=ids,
        metadatas=metadatas
    )

    print("✅ Saved", len(chunks), "chunks")
