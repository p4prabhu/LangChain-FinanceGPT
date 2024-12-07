# News Research Tool
A Streamlit-based application that enables users to extract, process, and query information from news articles. It uses OpenAI embeddings and FAISS for indexing and retrieval, allowing users to ask questions and get answers with relevant sources cited.

# Features
#^ Input URLs: Add up to three news article URLs in the sidebar for processing.
#^  Content Splitting: Automatically splits article content into manageable chunks for efficient processing.
#^  Embeddings Creation: Uses OpenAI embeddings to generate vector representations of the article content.
#^  FAISS Indexing: Stores embeddings in a FAISS index for fast similarity search and retrieval.
#^  Question Answering: Ask questions about the articles and get concise answers along with source citations.
#^  Persistent Index: Saves the FAISS index locally for reuse without reprocessing the URLs.
#^  Environment Security: Includes a .gitignore file to exclude sensitive .env files from being pushed to GitHub.
