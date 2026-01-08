import os
from langchain_openai import ChatOpenAI
# from langchain.chains import ConversationalRetrievalChain 
from langchain_classic.chains import ConversationalRetrievalChain
from langchain_chroma import Chroma
from langchain_huggingface import HuggingFaceEmbeddings
from config import CHROMA_PATH, EMBEDDING_MODEL_NAME

def get_conversation_chain():
    # 1. Setup Embeddings
    embeddings = HuggingFaceEmbeddings(model_name=EMBEDDING_MODEL_NAME)
    vector_store = Chroma(persist_directory=CHROMA_PATH, embedding_function=embeddings)
    
    # 2. OpenRouter LLM
    llm = ChatOpenAI(
        
        model_name="meta-llama/llama-3.3-70b-instruct:free", 
        
        # Connect to OpenRouter
        openai_api_key=os.environ.get("OPENROUTER_API_KEY"),
        openai_api_base="https://openrouter.ai/api/v1",
        
        temperature=0.5
    )

    # 3. Create the Chain (Simple version, no custom prompt)
    chain = ConversationalRetrievalChain.from_llm(
        llm=llm,
        retriever=vector_store.as_retriever(search_kwargs={"k": 3}),
        return_source_documents=True
    )
    return chain

