# app.py
import streamlit as st
from dotenv import load_dotenv
import os

load_dotenv()

st.set_page_config(page_title="Agentic RAG App")

st.title("Agentic RAG Demo")

query = st.text_input("Ask a question:")

if st.button("Submit"):
    st.write("Simulated response:")
    st.write("This is a placeholder response from the Agentic RAG pipeline.")

st.divider()
st.subheader("agentic_rag.ipynb preview")

try:
    with open("agentic_rag.ipynb", "r", encoding="utf-8") as f:
        st.text(f.read()[:1500])
except Exception:
    st.warning("Could not load agentic_rag.ipynb")
