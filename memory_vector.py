from sentence_transformers import SentenceTransformer
import chromadb
from chromadb.config import Settings
import uuid

embedding_model = SentenceTransformer("all-MiniLM-L6-v2")
client = chromadb.Client(Settings())
collection = client.get_or_create_collection(name="chat_memory")

def store_vector(session_id, text):
    embedding = embedding_model.encode(text).tolist()

    collection.add(
        documents=[text],
        embeddings=[embedding],
        ids=[str(uuid.uuid4())],
        metadatas=[{"session_id": session_id}]
    )
#search function 
def retrieve_vector(session_id, query, k=3):
    query_embedding = embedding_model.encode(query).tolist()

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=k,
        where={"session_id": session_id}
    )

    return results.get("documents", [[]])[0]
