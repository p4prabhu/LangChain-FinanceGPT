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



from dotenv import load_dotenv
load_dotenv()

import streamlit as st

st.title("News Research Tool")

st.sidebar.title("News Article URLs")

urls = []
for i in range(3):
    url = st.sidebar.text_input(f"URL {i+1}")
    urls.append(url)

process_url_clicked = st.sidebar.button("Process URLs")
file_path="faiss_store_openai.pkl"

main_placeholder=st.empty()
llm = OpenAI(temperature=0.9, max_tokens=500)

if process_url_clicked:
    # Load data
    loader = UnstructuredURLLoader(urls=urls)
    main_placeholder.text("Data is loading...")
    data = loader.load()

    # Split data
    text_splitter = RecursiveCharacterTextSplitter(
        separators=["\n\n", "\n", ".", " "],
        chunk_size=1000
    )
    main_placeholder.text("Text Splitter... Started... ✅✅✅")
    docs = text_splitter.split_documents(data)

    # Create embeddings and save to FAISS index
    embeddings = OpenAIEmbeddings()
    vectorstore_openai = FAISS.from_documents(docs, embeddings)
    main_placeholder.text("Embedding Vector Started Building... ✅✅✅")
    time.sleep(2)

    # Save the FAISS index to a pickle file
    vectorstore_openai.save_local("faiss_index_openai")
main_placeholder.text("Process Completed. FAISS Index Saved! 🎉")

query = main_placeholder.text_input("Question: ")
if query:
    if os.path.exists("faiss_index_openai"):
        # Load the FAISS index using FAISS's native method with deserialization allowed
        embeddings = OpenAIEmbeddings()
        vectorstore = FAISS.load_local(
            "faiss_index_openai", 
            embeddings, 
            allow_dangerous_deserialization=True
        )
        
        # Create the retrieval chain
        chain = RetrievalQAWithSourcesChain.from_llm(
            llm=llm, 
            retriever=vectorstore.as_retriever()
        )
        
        # Get the result from the chain
        result = chain({"question": query}, return_only_outputs=True)
        
        # Display the answer
        st.header("Answer")
        st.subheader(result["answer"])

        # Display sources, if available
        sources = result.get("sources", "")
        if sources:
            st.subheader("Sources:")
            sources_list = sources.split("\n")  # Split the sources by new line
            for source in sources_list:
                st.write(source)
