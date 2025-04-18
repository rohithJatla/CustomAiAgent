from embedding.embedder import embed_text
from embedding.vector_store import search_index
from ai_engine.summarizer import summarize_text

def answer_user_query(user_query):
    query_vec = embed_text([user_query])[0]
    context_chunks = search_index(query_vec)

    combined_context = "\n\n".join(context_chunks)
    if len(combined_context.split()) > 1000:
        combined_context = summarize_text(combined_context)

    prompt = f"""You are a helpful assistant. Answer only using the context below.

Context:
{combined_context}

Question: {user_query}

Answer:"""

    return prompt
