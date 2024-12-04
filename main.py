# imports
import os
import time
import pickle 
from langchain import OpenAI
import streamlit as st
import langchain 
from joblib import dump, load
from langchain.chains import RetrievalQAWithSourcesChain
from langchain.chains.qa_with_sources.loading import load_qa_with_sources_chain
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS



# Load environment variables from the `.env` file
from dotenv import load_dotenv
load_dotenv()

# Streamlit application UI setup
import streamlit as st

# App title displayed in the main UI
st.title("News Research Tool")

# Sidebar title for collecting URLs
st.sidebar.title("News Article URLs")

# URL input from the user
urls = []
for i in range(3):  # Collects up to 3 URLs from the user
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

# Button to start the URL processing
process_url_clicked = st.sidebar.button("Process URLs")
file_path = "faiss_store_openai.pkl"  # File path for storing the FAISS index

# Placeholder to display processing messages
main_placeholder = st.empty()

# Initialize the OpenAI LLM with specific parameters
llm = OpenAI(temperature=0.9, max_tokens=500)

if process_url_clicked:
    # Load data from the provided URLs
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data is loading...")
    data = loader.load()  # Fetch content from URLs

    # Split the loaded data into manageable chunks using RecursiveCharacterTextSplitter
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "],  # Splitting criteria
        chunk_size=1000  # Maximum size of each chunk
    )
    main_placeholder.text("Text Splitter... Started... ✅✅✅")
    docs = text_splitter.split_documents(data)  # Splits data into chunks

    # Generate embeddings for the document chunks using OpenAIEmbeddings
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)  # Create a FAISS vector store
    main_placeholder.text("Embedding Vector Started Building... ✅✅✅")
    time.sleep(2)

    # Save the FAISS index to a local file
    vectorstore_openai.save_local("faiss_index_openai")
main_placeholder.text("Process Completed. FAISS Index Saved! 🎉")

# Query input box for users to ask questions
query = main_placeholder.text_input("Question: ")
if query:
    # Check if the FAISS index exists locally
    if os.path.exists("faiss_index_openai"):
        # Load the saved FAISS index
        embeddings = OpenAIEmbeddings()  # Reinitialize embeddings
        vectorstore = FAISS.load_local(
            "faiss_index_openai",  # Path to the saved FAISS index
            embeddings,  # Load embeddings
            allow_dangerous_deserialization=True  # Allow deserialization (note: handle cautiously)
        )
        
        # Create a RetrievalQAWithSourcesChain for question-answering
        chain = RetrievalQAWithSourcesChain.from_llm(
            llm=llm,  # LLM instance
            retriever=vectorstore.as_retriever()  # Use FAISS as the retriever
        )
        
        # Use the retrieval chain to answer the user's query
        result = chain({"question": query}, return_only_outputs=True)
        
        # Display the retrieved answer in the Streamlit app
        st.header("Answer")
        st.subheader(result["answer"])

        # Display the sources for the answer, if available
        sources = result.get("sources", "")
        if sources:
            st.subheader("Sources:")
            sources_list = sources.split("\n")  # Split the sources by line
            for source in sources_list:  # Display each source
                st.write(source)