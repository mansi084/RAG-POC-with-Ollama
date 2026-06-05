from fastapi import FastAPI, UploadFile, File #Create the API app, handles uploaded files from user, tells FastAPI "this parameter is a file"
from pydantic import BaseModel #Helps define the structure of request data — like what a question request should look like
import shutil #Helps copy the uploaded file and save it to your documents folder
import os #Helps handle file paths and folder operations
from rag_service import RAGService #Imports your RAGService class — the brain of the entire project

app = FastAPI() #creates fast api app

rag_service = RAGService() #Create RAGService object

class QuestionRequest(BaseModel): #This is the structure of the question request
    question: str

# Endpoint 1 — Upload and train on a document
@app.post("/upload")
async def upload_document(file: UploadFile = File(...)):
    # Step 1 - Save uploaded file to documents folder
    file_path = f"./documents/{file.filename}"
    with open(file_path, "wb") as f:
        shutil.copyfileobj(file.file, f)

    # Step 2 - Train RAG on this file
    result = rag_service.train(file_path)

    return {"message": result}


# Endpoint 2 — Ask a question
@app.post("/ask")
async def ask_question(request: QuestionRequest):
    # Get answer from RAG
    answer = rag_service.ask(request.question)

    return {"answer": answer}

