# RAG POC with Ollama

> Ask questions from your own documents — privately, freely, and fully offline.

No ChatGPT. No API keys. No data leaving your machine.
Just upload a document, ask a question, get an answer.

---

## What is this?

A **Proof of Concept** for a **RAG (Retrieval Augmented Generation)** system that:

1. Takes your documents (PDF, TXT, DOCX)
2. Splits them into chunks
3. Converts chunks into vectors (embeddings)
4. Stores vectors locally in ChromaDB
5. When you ask a question — finds the most relevant chunks
6. Sends those chunks as context to a local LLM
7. Returns an accurate answer based on YOUR documents

---

## Architecture

TRAINING FLOW:
Your Document
↓
Document Loader (PDF / TXT / DOCX)
↓
Text Splitter (chunks of 500 chars)
↓
nomic-embed-text (converts to vectors)
↓
ChromaDB (saves vectors locally)


QUERY FLOW:
User asks a Question
↓
nomic-embed-text (converts question to vector)
↓
ChromaDB (finds top 3 similar chunks)
↓
Llama3 via Ollama (reads chunks + generates answer)
↓
Answer returned to user

---

## Project Structure

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

---

## Tech Stack

| Tool | Version | Purpose |
|---|---|---|
| **Python** | 3.11 | Core language |
| **Ollama** | Latest | Runs AI models locally |
| **Llama3** | Latest | LLM that reads and answers |
| **nomic-embed-text** | Latest | Converts text to vectors |
| **ChromaDB** | Latest | Stores and searches vectors |
| **LangChain** | Latest | Connects all components |
| **FastAPI** | Latest | REST API framework |
| **Uvicorn** | Latest | ASGI server |

---

## Prerequisites

- Python 3.10 or higher
- Ollama installed → [Download here](https://ollama.com)
- Git installed
- 8GB RAM minimum (16GB recommended)
- 10GB free disk space

---

## Setup & Installation

### Step 1 — Clone the repository
```bash
git clone https://github.com/mansi084/RAG-POC-with-Ollama
cd RAG-POC-with-Ollama
```

### Step 2 — Create virtual environment
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# Mac/Linux
python -m venv venv
source venv/bin/activate
```

### Step 3 — Install dependencies
```bash
pip install -r requirements.txt
```

### Step 4 — Pull Ollama models
```bash
# Pull the LLM
ollama pull llama3

# Pull the embedding model
ollama pull nomic-embed-text
```

### Step 5 — Start the server
```bash
uvicorn app:app --reload
```

### Step 6 — Open API docs in browser
http://127.0.0.1:8000/docs

---

## API Endpoints

### Upload a Document
POST /upload
Accepts: PDF, TXT, DOCX

Example using Swagger UI:
- Go to `http://127.0.0.1:8000/docs`
- Click `POST /upload`
- Click `Try it out`
- Choose your file
- Click `Execute`

Response:
```json
{
  "message": "Successfully trained on 12 chunks!"
}
```

---

### Ask a Question
POST /ask
Example request:
```json
{
  "question": "What is the leave policy?"
}
```

Example response:
```json
{
  "answer": "According to the policy, every employee gets 20 paid leaves per year."
}
```

---

## Configuration

Everything is controlled from `config.yaml`:

```yaml
llm:
  provider: ollama
  model: llama3          

embedding:
  provider: ollama
  model: nomic-embed-text

vectorstore:
  provider: chroma
  path: ./my_database

chunking:
  chunk_size: 500
  chunk_overlap: 50
```

### Swap models in seconds — no code changes needed!
```yaml
# Want Mistral instead of Llama3?
llm:
  model: mistral   ← just change this one line!
```

---

##  Supported File Types

PDF
Word Document
Plain Text 

---

## Features

- 100% local — no internet needed
- Free — no API costs
- Private — data never leaves your PC
- Pluggable — swap models via config
- Semantic search — finds meaning not just keywords
- Supports PDF, TXT, DOCX
- REST API powered by FastAPI
- Auto-generated API docs at `/docs`
- ChromaDB persists data between restarts

---

## Privacy

-  All processing happens on your machine
-  No data sent to any external server
-  Works completely offline
-  Your documents never leave your PC

---










