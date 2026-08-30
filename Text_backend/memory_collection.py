import ollama

from langchain_community.vectorstores import FAISS
from langchain_huggingface import HuggingFaceEmbeddings


# ============================================================
# Doctor-GPT Text Backend
# ============================================================

DB_FAISS_PATH = "medical-chatbot/vectorstore/db_faiss"

EMBEDDING_MODEL = "sentence-transformers/all-MiniLM-L6-v2"


def doctor_gpt_backend(query: str) -> str:
    """
    Text chatbot backend.

    Retrieves relevant medical information from FAISS
    and sends it to the local Ollama model.
    """

    try:
        # ----------------------------------------------------
        # Load embedding model
        # ----------------------------------------------------

        embedding_model = HuggingFaceEmbeddings(
            model_name=EMBEDDING_MODEL
        )

        # ----------------------------------------------------
        # Load FAISS database
        # ----------------------------------------------------

        db = FAISS.load_local(
            DB_FAISS_PATH,
            embedding_model,
            allow_dangerous_deserialization=True,
        )

        # ----------------------------------------------------
        # Retrieve relevant documents
        # ----------------------------------------------------

        retriever = db.as_retriever(
            search_kwargs={"k": 3}
        )

        documents = retriever.invoke(query)

        context = "\n\n".join(
            document.page_content
            for document in documents
        )

        # ----------------------------------------------------
        # Prompt
        # ----------------------------------------------------

        prompt = f"""
You are Doctor-GPT, a medical information assistant.

Use the provided medical context to answer the user's question.

Rules:
- Give clear and simple medical information.
- Do not claim to diagnose a disease with certainty.
- Do not prescribe medicines or dosages.
- If the information is not available in the context, say that
  you do not have enough information.
- For serious or emergency symptoms, recommend professional
  medical help.

MEDICAL CONTEXT:
{context}

USER QUESTION:
{query}

ANSWER:
"""

        # ----------------------------------------------------
        # Ollama
        # ----------------------------------------------------

        response = ollama.chat(
            model="qwen2.5:3b",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
            options={
                "temperature": 0.3,
                "num_predict": 400,
            },
        )

        return response["message"]["content"].strip()

    except Exception as e:

        print("TEXT BACKEND ERROR:", repr(e))

        return (
            "I'm unable to access the medical knowledge base "
            "right now. Please try again shortly."
        )