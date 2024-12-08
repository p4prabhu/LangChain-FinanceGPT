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
### 1. Clone the Repository
1. **Clone this repository** to your local machine using:**
   ```bash
   git clone https://github.com/p4prabhu/LangChain-FinanceGPT.git
2. **Navigate to the project directory:**
   ```bash
   cd LangChain-FinanceGPT
3. **Create and activate a virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate
4. **Install the required dependencies using pip:**
   ```bash
   pip install -r requirements.txt
5. **Set up your OpenAI API key**:
   - **Create a file named `.env`** in the project root.
   - **Add your API key** in the following format:
     ```plaintext
     OPENAI_API_KEY=your_api_key_here
     ```
   
   ◊
   
   
   




  

