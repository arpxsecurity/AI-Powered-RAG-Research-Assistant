# AI Powered RAG Research Assistant
<img width="1536" height="1024" alt="AI Powered RAG Research Assistant Banner" src="https://github.com/user-attachments/assets/21179c4f-08bf-429f-bac7-b392c397a408" />

This project is an AI-powered Research Assistant built using a Retrieval-Augmented Generation (RAG) approach.
The goal of this application is to help users search, process, and interact with scientific research papers from the ArXiv repository using natural language queries.

Instead of relying only on a language model’s internal knowledge, the system retrieves relevant content from real research papers, stores them as vector embeddings, and generates responses grounded in the retrieved documents.

---

## Why this project?

Reading and analyzing multiple research papers is time-consuming.  
This project automates:
- Research paper retrieval from ArXiv
- PDF content extraction
- Semantic search over papers
- Question answering based on actual paper content

Unlike many constrained demo systems, this application is not strictly limited by hardware.
It is designed to scale based on the available system resources and configuration, allowing it to run efficiently on local machines, high-performance systems, or cloud environments with adjustable limits.

---

## Core Functionality

- Fetches research papers using the **ArXiv API**
- Downloads and parses PDFs using **PyPDF**
- Splits and embeds documents for efficient retrieval
- Stores embeddings in **ChromaDB**
- Uses a **RAG pipeline** via LangChain for context-aware responses
- Exposes backend functionality through a **FastAPI-powered API**
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

├── api.py            # FastAPI backend endpoints

├── ui.py             # Streamlit user interface

├── index.py          # Embedding & vector indexing logic

├── conversation.py   # RAG-based conversation handling

├── arxiv_call.py     # ArXiv API integration

├── config.py         # Configuration and system limits

├── requirement.txt   # Python dependencies

└── README.md

---

## How the RAG Pipeline Works

1. User searches for a research topic
2. Relevant papers are fetched from ArXiv
3. PDFs are downloaded and text is extracted
4. Extracted text is chunked and transformed into vector embeddings
5. These embeddings are stored in a vector database (ChromaDB) for efficient similarity search
6. User questions are matched against stored vectors to retrieve the most relevant context
7. The LLM generates answers grounded in the retrieved research content

This approach ensures that responses are based on actual research papers rather than hallucinated information.

---

## Architecture Overview

The system follows a modular, service-oriented architecture designed for scalability and flexibility.

- The user interacts with the system through a Streamlit-based web interface.
- User requests are sent to a FastAPI backend that manages the application logic.
- Research papers are fetched from the ArXiv API based on user queries.
- PDFs are downloaded and processed to extract textual content.
- Extracted text is converted into vector embeddings.
- Embeddings are stored in ChromaDB for efficient semantic search.
- Relevant document chunks are retrieved based on user queries.
- A Large Language Model (LLM) generates context-aware responses using retrieved data.

This architecture allows independent scaling of components such as the backend, vector store, and LLM integration.

---

## Setup Instructions

### Step 1: Clone the repository
git clone https://github.com/arpxsecurity/AI-Powered-RAG-Research-Assistant.git

cd AI-Powered-RAG-Research-Assistant

Step 2: Install dependencies

pip install -r requirement.txt

Step 3: Start Backend

python api.py

Step 4: Start Frontend

python -m streamlit run ui.py

Step 5: Access Application

Copy the Streamlit URL from the terminal and open it in your browser.

## Configuration Notes :

- If hardware resources are limited, it is recommended to restrict the number of papers processed at a time for better performance.
- The default token limit is set to 10k tokens per paper, but this is not a fixed limitation and can be adjusted easily via config.py based on system capability.
- The system is flexible and can be scaled up or down depending on available memory, compute power, and use case requirements.
- OpenRouter is used for demo/testing instead of direct OpenAI API

## Limitations :

- The system is designed primarily for research assistance, exploration, and understanding, not for generating full-length academic papers.
- It focuses on retrieval, summarization, and question answering rather than original paper authorship.
- Performance depends on document size, number of papers, system resources (Memory), and internet speed especially during large-scale indexing tasks.
- Not optimized for very large-scale batch processing

## Future Scope

- Support for additional research sources beyond ArXiv (e.g., PubMed, IEEE, Semantic Scholar)
- Integration with more advanced vector databases for large-scale deployments
- Multi-document comparison and cross-paper reasoning
- Improved chunking and embedding strategies for better retrieval accuracy
- User authentication and saved research sessions
- Batch document ingestion for enterprise-level use cases
- Deployment-ready configurations for cloud and containerized environments

## Use Cases :

- Research paper exploration and semantic search
- Academic literature review and comparison
- Understanding complex papers using natural language
- Experimenting with RAG-based AI systems
- Assisting HR teams in analyzing thousands of resumes simultaneously using document embeddings and semantic search
- Designed primarily for research assistance and document intelligence, not full paper generation

## Development Timeline

- **Project Type:** Self-driven research project  
- **Duration:** Aug - Nov 2025  
- **Focus:** RAG-based research paper retrieval and semantic question answering using ArXiv data

