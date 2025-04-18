import faiss
import numpy as np

dimension = 384
index = faiss.IndexFlatL2(dimension)
doc_texts = []

def add_to_index(text, embedding):
    global index, doc_texts
    embedding = np.expand_dims(embedding, axis=0)
    index.add(embedding)
    doc_texts.append(text)

def search_index(query_embedding, top_k=3):
    global index
    D, I = index.search(np.expand_dims(query_embedding, axis=0), top_k)
    return [doc_texts[i] for i in I[0]]
