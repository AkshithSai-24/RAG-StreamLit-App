import streamlit as st
from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, TextLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_community.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains import RetrievalQA
import tempfile
import os
from dotenv import load_dotenv
load_dotenv()


st.set_page_config(page_title="Document Chat with RAG ", layout="wide")
st.title("RAG Streamlit Application")
st.markdown("📄 Chat with your Documents using RAG ",unsafe_allow_html=True)


uploaded_files = st.file_uploader("Upload Documents", type=["pdf", "docx", "txt"], accept_multiple_files=True)

docs = []

if uploaded_files:
    for uploaded_file in uploaded_files:
        with tempfile.NamedTemporaryFile(delete=False) as tmp_file:
            tmp_file.write(uploaded_file.read())
            tmp_path = tmp_file.name

        if uploaded_file.name.endswith(".pdf"):     # Load PDF files
            loader = PyPDFLoader(tmp_path)
        elif uploaded_file.name.endswith(".docx"):  # Load DOCX files
            loader = Docx2txtLoader(tmp_path)
        elif uploaded_file.name.endswith(".txt"):   # Load TXT files
            loader = TextLoader(tmp_path)
        else:
            st.warning(f"Unsupported file type: {uploaded_file.name}")
            continue

        docs.extend(loader.load())
        os.remove(tmp_path)

    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)   # Split documents into manageable chunks
    chunks = splitter.split_documents(docs) 


    embeddings = GoogleGenerativeAIEmbeddings(model="models/text-embedding-004")    # Initialize embeddings using Google Generative AI

    vectordb = FAISS.from_documents(chunks, embeddings)   # Create a vector store from the document chunks

    retriever = vectordb.as_retriever() # Create a retriever from the vector store

    llm = ChatGoogleGenerativeAI(model="models/gemini-2.0-flash")   # Initialize the LLM using Google Generative AI

    qa_chain = RetrievalQA.from_chain_type(llm=llm, retriever=retriever)       # Create a QA chain for question answering

    st.markdown("---")
    st.subheader("Ask a question about your documents")
    user_query = st.text_input("Enter your question:")

    if user_query:
        response = qa_chain.invoke(user_query)  # Invoke the QA chain with the user's query
        st.markdown("### Answer")
        st.write(response['result'])  # Display the answer from the QA chain
        

else:
    st.info("Please upload documents to begin.")
    st.markdown("---")
    # Add a persistent footer using Streamlit's markdown and CSS
    footer = """
        <style>
            .footer {
                position: fixed;
                left: 0;
                bottom: 0;
                width: 100%;
                background-color: #f0f2f6;
                color: gray;
                text-align: center;
                padding: 10px 0;
                z-index: 100;
            }
            /* Prevent Streamlit's main block from overlapping the footer */
            .block-container {
                padding-bottom: 60px;
            }
        </style>
        <div class="footer">
            Developed by Akshith Sai Kondamadugu
        </div>
    """
    st.markdown(footer, unsafe_allow_html=True)