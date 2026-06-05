# It is an empty file that tells Python "this folder is a package" so you can import files from it.

#The factories folder is just a place where all your "decision makers" live. 
# It decides WHICH thing to give based on what's asked!

#rag_service.py says "give me an embedding model"
#       ↓
# embedding_factory.py decides:
#   "ollama? openai? huggingface?"
#       ↓
# returns the right one based on config.yaml

#Why keep them in a separate folder?
# Because rag_service.py doesn't need to know HOW to create each component — it just asks the factory

#factories folder contains decision-making files — each one reads the config and returns the 
# right component, so the rest of your code never needs to worry about which specific tool is 
# being used.