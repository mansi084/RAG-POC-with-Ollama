# RAG POC with Ollama

A simple Retrieval-Augmented Generation (RAG) Proof of Concept that uses local documents and a local LLM running through Ollama to answer user queries.

# Overview

This project demonstrates a basic RAG pipeline:

1. Load documents (PDF, DOCX, TXT)
2. Split documents into chunks
3. Generate embeddings
4. Store embeddings in a vector database
5. Retrieve relevant chunks for a user query
6. Send retrieved context to an Ollama model
7. Generate an answer

# Architecture

User Query
    ↓
Retriever
    ↓
Vector Database
    ↓
Relevant Chunks
    ↓
Ollama LLM
    ↓
Generated Answer


Documents
   ↓
Chunking
   ↓
Embeddings
   ↓
Vector DB
   ↓
Retriever
   ↓
Ollama
   ↓
Answer


# Tech Stack

- Python 3.11
- Ollama
- LangChain
- ChromaDB
- Sentence Transformers
- Streamlit (optional UI)


# Project Structure

project/
├── config.yaml                  → all settings
├── app.py                       → FastAPI endpoints
├── rag_service.py               → core RAG logic
├── factories/
│   ├── embedding_factory.py     → picks embedding model
│   ├── llm_factory.py           → picks LLM
│   └── vectorstore_factory.py   → picks vector DB
├── loaders/
│   └── document_loader.py       → reads PDF/TXT/DOCX
├── documents/                   → drop your files here
└── my_database/                 → ChromaDB saves here


# Prerequisites

- Python 3.10+
- Ollama installed
- Git


# Pull Ollama Model

ollama pull llama3


# Installation

Clone repository
git clone <repository-url>
cd project
Install dependencies
pip install -r requirements.txt


# Run

Step 1: Start Ollama
ollama serve
Step 2: Create Vector Database
python src/ingest.py
Step 3: Run Application
python app.py


# Features

- Local LLM using Ollama
- No external API dependency
- Semantic search
- Document-based Q&A
- Easy to extend




