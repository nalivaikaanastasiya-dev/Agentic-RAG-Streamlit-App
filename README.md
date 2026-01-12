# Agentic-RAG-Streamlit-App

Daily Challenge project: an Agentic RAG app with Streamlit + LangChain.

## What this repo contains

- `app.py` – Streamlit UI scaffold
- `agentic_rag.ipynb` – notebook with agent + RAG logic
- `.env` – API keys
- `requirements.txt` – dependencies

## Setup

```bash
pip install -r requirements.txt
cp .env.example .env
# add your keys
streamlit run app.py
