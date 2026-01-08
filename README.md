# AI Powered RAG Research Assistant
<img width="1536" height="1024" alt="ChatGPT Image Jan 8, 2026, 12_39_16 PM" src="https://github.com/user-attachments/assets/d09f3aa0-8271-4733-8cad-b9d1ed0f675d" />

This project is an AI-powered Research Assistant built using a Retrieval-Augmented Generation (RAG) approach.  
The goal of this application is to help users search, process, and interact with scientific research papers from the ArXiv repository using natural language queries.

Instead of relying only on a language model’s knowledge, the system retrieves relevant content from real research papers, stores them as vector embeddings, and generates answers grounded in the retrieved documents.

---

## Why this project?

Reading and analyzing multiple research papers is time-consuming.  
This project automates:
- Research paper retrieval from ArXiv
- PDF content extraction
- Semantic search over papers
- Question answering based on actual paper content

The system is designed with performance limits in mind so it can run on local machines or limited cloud resources.

---

## Core Functionality

- Fetches research papers using the **ArXiv API**
- Downloads and parses PDFs using **PyPDF**
- Splits and embeds documents for efficient retrieval
- Stores embeddings in **ChromaDB**
- Uses a **RAG pipeline** via LangChain for grounded responses
- Provides a REST API using **FastAPI**
- Offers an interactive user interface using **Streamlit**

---

## Tech Stack

- **Language:** Python  
- **Backend:** FastAPI  
- **Frontend:** Streamlit  
- **LLM Framework:** LangChain  
- **Vector Database:** ChromaDB  
- **LLM Provider:** OpenAI / OpenRouter  
- **Data Source:** ArXiv API  
- **PDF Processing:** PyPDF  

---

## Project Structure

├── api.py # FastAPI backend endpoints
├── ui.py # Streamlit user interface
├── index.py # Embedding & vector indexing logic
├── conversation.py # RAG-based conversation handling
├── arxiv_call.py # ArXiv API integration
├── config.py # Configuration and system limits
├── requirement.txt # Python dependencies
└── README.md



---

## How the RAG Pipeline Works

1. User searches for a research topic
2. Relevant papers are fetched from ArXiv
3. PDFs are downloaded and text is extracted
4. Text is chunked and converted into embeddings
5. Embeddings are stored in ChromaDB
6. User questions are matched with relevant chunks
7. The LLM generates answers based on retrieved context

This ensures responses are based on actual research papers, not hallucinations.

---

## Setup Instructions

### Step 1: Clone the repository
git clone https://github.com/arpxsecurity//AI-Powered-RAG-Application.git
cd AI-Powered-RAG-Application

Step 2: Install dependencies

pip install -r requirement.txt

Step 3: Start Backend

python api.py

Step 4: Start Frontend

streamlit run ui.py

Step 5: Access Application

Copy the Streamlit URL from the terminal and open it in your browser.

* Configuration Notes :

Avoid processing more than 10 research papers at a time
Large document processing may be slow on cloud or free GPU environments
Token limit is set to 10k per paper (configurable in config.py)
OpenRouter is used for demo/testing instead of direct OpenAI API

* Limitations :

Not optimized for very large-scale batch processing
Performance depends on system memory and internet speed
Designed primarily for research assistance, not full paper generation

* Use Cases :

Research paper exploration
Academic literature review
Understanding complex papers using natural language
Experimenting with RAG-based AI systems

* Resume Description (Reference) :

AI Powered RAG Research Assistant | Self Project (Nov 2025)

Built a Retrieval-Augmented Generation based research assistant that retrieves, processes, and enables semantic querying of scientific papers from ArXiv using FastAPI, Streamlit, LangChain, and ChromaDB.

