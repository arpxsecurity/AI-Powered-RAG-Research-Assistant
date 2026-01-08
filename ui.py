import streamlit as st
import requests

# URL of our FastAPI Backend
API_URL = "http://localhost:8000"

st.set_page_config(page_title="AI-powered Assistant", layout="wide", page_icon=" ")

# Custom CSS for better looking citations
st.markdown("""
<style>
    .citation-box {
        border-left: 3px solid #ff4b4b;
        padding-left: 10px;
        margin-top: 5px;
        background-color: #f0f2f6;
        padding: 10px;
        border-radius: 5px;
    }
</style>
""", unsafe_allow_html=True)

st.title("AI-powered Research Paper Assistant")

# Initialize Chat History
if "messages" not in st.session_state:
    st.session_state.messages = []
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Tabs
tab1, tab2 = st.tabs(["Step 1: Research & Index", "Step 2: Chat & Analysis"])

# --- TAB 1: INGESTION ---
with tab1:
    st.header("Find & Index Research Papers")
    st.write("Search ArXiv to build your knowledge base.")
    
    col1, col2 = st.columns([3, 1])
    query = col1.text_input("Research Topic", "cs.AI")
    num_papers = col2.number_input("Number of Papers", 1, 10000, 3)

    if st.button("Start Research", type="primary"):
        with st.status("Agent is working...", expanded=True) as status:
            try:
                st.write("🔍 Searching ArXiv and downloading PDFs...")
                payload = {"query": query, "max_results": num_papers}
                response = requests.post(f"{API_URL}/ingest", json=payload)
                
                if response.status_code == 200:
                    data = response.json()
                    st.code(data.get("log"))
                    status.update(label="Indexing Complete!", state="complete", expanded=False)
                    st.success("Knowledge Base Updated! Go to the Chat tab.")
                else:
                    st.error(f"Error: {response.text}")
                    status.update(label="Failed", state="error")
            except Exception as e:
                st.error(f"Connection Error: Is the backend running? {e}")

# --- TAB 2: CHAT ---
with tab2:
    st.header("Chat with Papers")
    
    # Display History
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    if prompt := st.chat_input("Ask about the research (e.g., 'Compare the methodologies')..."):
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)

        with st.chat_message("assistant"):
            with st.spinner("Analyzing papers..."):
                try:
                    payload = {
                        "question": prompt,
                        "chat_history": st.session_state.chat_history
                    }
                    response = requests.post(f"{API_URL}/chat", json=payload)
                    
                    if response.status_code == 200:
                        data = response.json()
                        answer = data["answer"]
                        sources = data.get("sources", [])
                        
                        # 1. Show the Answer
                        st.markdown(answer)
                        
                        # 2. Show Citations (New Feature)
                        if sources:
                            with st.expander("Referenced Sources From ArXiv"):
                                seen_sources = set()
                                for source in sources:
                                    # Create a unique key to avoid duplicates
                                    source_key = source.get('title', 'Unknown')
                                    if source_key not in seen_sources:
                                        st.markdown(f"""
                                        <div class="citation-box">
                                            <b>📄 {source.get('title', 'Unknown Title')}</b><br>
                                            <small>👤 {source.get('authors', 'Unknown Authors')} | 📅 {source.get('published', 'N/A')}</small><br>
                                            <a href="{source.get('source_url', '#')}" target="_blank">🔗 View on ArXiv</a>
                                        </div>
                                        """, unsafe_allow_html=True)
                                        seen_sources.add(source_key)

                        # Update history
                        st.session_state.chat_history.append((prompt, answer))
                        st.session_state.messages.append({"role": "assistant", "content": answer})
                        
                    else:
                        st.error(f"Backend Error: {response.text}")
                except Exception as e:
                    st.error(f"Connection Error: Is the backend running? {e}")