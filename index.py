from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from config import CHROMA_PATH, EMBEDDING_MODEL_NAME, CHUNK_SIZE, CHUNK_OVERLAP

def create_vector_db(papers_data):
    """
    Receives a list of dicts (path, title, authors, etc.)
    """
    if not papers_data:
        return "No files provided."

    all_splits = []

    for paper in papers_data:
        try:
            loader = PyPDFLoader(paper["path"])
            docs = loader.load()
            
            #  METADATA (Crucial for Filters)
            for doc in docs:
                doc.metadata.update({
                    "title": paper["title"],
                    "authors": paper["authors"],
                    "published": paper["published"],
                    "source_url": paper["url"],
                    "arxiv_id": paper["id"]
                })
                
            all_splits.extend(docs)
        except Exception as e:
            print(f"Error loading {paper['title']}: {e}")

    if not all_splits:
        return "No valid text found."

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=CHUNK_SIZE, chunk_overlap=CHUNK_OVERLAP)
    texts = text_splitter.split_documents(all_splits)

    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    
    Chroma.from_documents(
        documents=texts,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )
    
    return f"Indexed {len(texts)} chunks from {len(papers_data)} papers."