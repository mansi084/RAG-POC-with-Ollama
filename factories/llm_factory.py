# Decide which LLM to create
from langchain_ollama import OllamaLLM  #Connects to your locally running Llama3 model via Ollama


def get_llm(config):
    provider = config["llm"]["provider"]
    model = config["llm"]["model"]

    if provider == "ollama":
        return OllamaLLM(model = model)

    else:
        raise ValueError(f"Unsupported LLM provider: {provider}")
    



