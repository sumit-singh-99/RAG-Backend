from app.database.vectordb import collection
from app.core.embeddings import embed_query


def retrieve_docs(query, k=8):

    query_embedding = embed_query(query)

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        include=["documents", "metadatas"]
    )

    docs = results.get("documents", [[]])[0]
    print(f"Retrieved {docs} documents from vector DB.")

    # Extra filter: keep only relevant chunks
    filtered = []

    for d in docs:
        if len(d) > 200:
            filtered.append(d)

    return filtered
