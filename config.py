import os
from dotenv import load_dotenv

# 1. Load the .env file immediately
load_dotenv()

# 2. Silent Check (No print unless error)
key = os.environ.get("OPENROUTER_API_KEY")

if not key:
    print("WARNING: OPENROUTER_API_KEY not found in .env file!")

# --- PATHS ---
DOWNLOAD_DIR = "downloaded_papers"
CHROMA_PATH = "./chroma_db"

# --- MODELS ---
EMBEDDING_MODEL_NAME = "sentence-transformers/all-mpnet-base-v2"
LLM_MODEL_NAME = "gpt-3.5-turbo" 

# --- SETTINGS ---
CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200

# Create directories if they don't exist
os.makedirs(DOWNLOAD_DIR, exist_ok=True)
os.makedirs(CHROMA_PATH, exist_ok=True)