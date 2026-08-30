import os
import streamlit as st
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq

from dotenv import load_dotenv, find_dotenv
load_dotenv(find_dotenv())

DB_FAISS_PATH = "vectorstore/db_faiss"

@st.cache_resource
def get_vectorstore():
    embedding_model = HuggingFaceEmbeddings(model_name='sentence-transformers/all-MiniLM-L6-v2')
    db = FAISS.load_local(DB_FAISS_PATH, embedding_model, allow_dangerous_deserialization=True)
    return db

def set_custom_prompt(custom_prompt_template):
    prompt = PromptTemplate(template=custom_prompt_template, input_variables=["context", "question"])
    return prompt

def format_docs(docs):
    return "\n\n".join(doc.page_content for doc in docs)

def load_llm():
    GROQ_API_KEY = os.environ.get("GROQ_API_KEY")
    llm = ChatGroq(
        model="llama-3.3-70b-versatile",
        temperature=0.5,
        api_key=GROQ_API_KEY
    )
    return llm

def main():
    st.title("Ask Chatbot!")

    if 'messages' not in st.session_state:
        st.session_state.messages = []

    for message in st.session_state.messages:
        st.chat_message(message['role']).markdown(message['content'])

    prompt = st.chat_input("Pass your prompt here")

    if prompt:
        st.chat_message('user').markdown(prompt)
        st.session_state.messages.append({'role': 'user', 'content': prompt})

        CUSTOM_PROMPT_TEMPLATE = """
                Use the pieces of information provided in the context to answer user's question.
                If you dont know the answer, just say that you dont know, dont try to make up an answer. 
                Dont provide anything out of the given context
                Context: {context}
                Question: {question}
                Start the answer directly. No small talk please.
                """

        try:
            vectorstore = get_vectorstore()
            if vectorstore is None:
                st.error("Failed to load the vector store")

            retriever = vectorstore.as_retriever(search_kwargs={'k': 3})

            rag_chain = (
                {"context": retriever | format_docs, "question": RunnablePassthrough()}
                | set_custom_prompt(CUSTOM_PROMPT_TEMPLATE)
                | load_llm()
                | StrOutputParser()
            )

            result = rag_chain.invoke(prompt)
            source_documents = retriever.invoke(prompt)

            result_to_show = result + "\nSource Docs:\n" + str(source_documents)

            st.chat_message('assistant').markdown(result_to_show)
            st.session_state.messages.append({'role': 'assistant', 'content': result_to_show})

        except Exception as e:
            st.error(f"Error: {str(e)}")

if __name__ == "__main__":
    main()