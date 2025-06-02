import torch
from transformers import AutoTokenizer, AutoModel
import faiss
import numpy as np

# Load model and tokenizer
MODEL_NAME = "sentence-transformers/all-MiniLM-L6-v2"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModel.from_pretrained(MODEL_NAME)

def embed_text(text):
    inputs = tokenizer(text, return_tensors="pt", padding=True, truncation=True)
    with torch.no_grad():
        outputs = model(**inputs)
        embeddings = outputs.last_hidden_state.mean(dim=1).squeeze().numpy()
    return embeddings

def build_vector_store(text_chunks):
    dim = len(embed_text("test"))
    index = faiss.IndexFlatL2(dim)
    embeddings = [embed_text(chunk) for chunk in text_chunks]
    index.add(np.array(embeddings))
    return index, text_chunks, embeddings

def search(index, query, texts, top_k=3):
    query_vec = embed_text(query).reshape(1, -1)
    distances, indices = index.search(query_vec, top_k)
    return [texts[i] for i in indices[0]]