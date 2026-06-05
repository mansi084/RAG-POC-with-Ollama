#Decide which embedding model to create
from langchain_ollama import OllamaEmbeddings #Converts text to vectors using nomic-embed-text via Ollama

def get_embedding_model(config):
    provider = config["embedding"]["provider"]
    model = config["embedding"]["model"]

    if provider == "ollama":
        return OllamaEmbeddings(model = model)
    else: 
        raise ValueError(f"Unsupported embedding provider: {provider}")
    
