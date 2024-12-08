# News Research Tool
A Streamlit-based application that enables users to extract, process, and query information from news articles. It uses OpenAI embeddings and FAISS for indexing and retrieval, allowing users to ask questions and get answers with relevant sources cited.

## Features

- **Input URLs**: Add up to three news article URLs in the sidebar for processing.
- **Content Splitting**: Automatically splits article content into manageable chunks for efficient processing.
- **Embeddings Creation**: Uses OpenAI embeddings to generate vector representations of the article content.
- **FAISS Indexing**: Stores embeddings in a FAISS index for fast similarity search and retrieval.
- **Question Answering**: Ask questions about the articles and get concise answers along with source citations.
- **Persistent Index**: Saves the FAISS index locally for reuse without reprocessing the URLs.
- **Environment Security**: Includes a `.gitignore` file to exclude sensitive `.env` files from being pushed to GitHub.

### Prerequisites

- **Python 3.8 or higher**: Ensure you have Python installed on your system. [Download Python here](https://www.python.org/downloads/) if not already installed.
- **OpenAI API Key**: Obtain an API key by signing up at [OpenAI](https://openai.com/). This key will be required for the application to function.

## Steps

1. **Input URLs**:
   - Open the application in your browser (usually `http://localhost:8501` after running `streamlit run main.py`).
   - Enter up to three news article URLs in the sidebar.

2. **Process URLs**:
   - Click the **Process URLs** button to fetch and process the content of the entered URLs.
   - The application will split the content into manageable chunks for processing.

3. **Ask Questions**:
   - Use the query box in the main interface to ask questions related to the articles.
   - Example: *"What is the main topic of the article?"* or *"What are the key highlights?"*

4. **View Answers**:
   - The application will retrieve answers to your questions using OpenAI embeddings and FAISS.
   - The result includes both the answer and the sources from which the information was extracted.

5. **Reuse the Index (Optional)**:
   - The FAISS index is saved locally (`faiss_index_openai` directory).
   - You can reuse it in future sessions without reprocessing the same URLs.
  

