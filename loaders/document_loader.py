import os #Helps handle files and folder paths on your computer
from langchain_community.document_loaders import PyPDFLoader #Reads and extracts text from PDF files
from langchain_community.document_loaders import TextLoader #Reads and extracts text from plain .txt files
from langchain_community.document_loaders import Docx2txtLoader #Reads and extracts text from Word .docx files



def load_document(file_path:str): #file_path(var) :(should be of type) str
        #picking correct loader as per type of file
        ext = os.path.splitext(file_path)[-1].lower() 
        #os.path.splitext() splits path into name + extension (used for file paths only)
        #[-1] picks the last part(extension)

        if ext == ".pdf":
            loader = PyPDFLoader(file_path)
        elif ext == ".txt":
            loader = TextLoader(file_path)
        elif ext == ".docx":
            loader = Docx2txtLoader(file_path)
        else:
            raise ValueError(f"Unsupported file type: {ext}")
        
        return loader.load() #.load() actually read the file and extract all the text in loader

