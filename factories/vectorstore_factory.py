# Decide which vector DB to create
from langchain_chroma import Chroma #Connects to ChromaDB to store and search vectors


def get_vectorstore(config, embedding): #Because ChromaDB needs an embedding model to function
    provider = config["vectorstore"]["provider"]
    if provider == "chroma":
        return Chroma(
            persist_directory = config["vectorstore"]["path"],
            embedding_function = embedding
        )

    else:
        raise ValueError(f"Unsupported vectorstore provider: {provider}")