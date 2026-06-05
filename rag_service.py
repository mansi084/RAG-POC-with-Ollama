from factories.embedding_factory import get_embedding_model #factory folder
from factories.llm_factory import get_llm
from factories.vectorstore_factory import get_vectorstore
from loaders.document_loader import load_document #loaders folder

import yaml #read config.yaml to this file

from langchain_text_splitters import RecursiveCharacterTextSplitter #Splits your documents into small chunks
from langchain_core.prompts import ChatPromptTemplate #Creates a template for how you ask questions to the LLM
from langchain_core.output_parsers import StrOutputParser #Converts LLM's response into a clean readable string
from langchain_core.runnables import RunnablePassthrough #Passes te user's question as it is through the chain without changing it


#train(): 1. Load document (using loaders) 2. Split into chunks (using splitter) 3. Save to ChromaDB (using vectorstore)
#ask() : 1. Create retriever from vectorstore 2. Create prompt template 3. Build chain → retriever | prompt | llm | parser 4. Return answer

class RAGService():
    def __init__(self):
        #loading config.yaml file
        with open("config.yaml","r") as f:
            self.config = yaml.safe_load(f) #converts yaml to dict format

        #calling embedding factory
        self.embedding = get_embedding_model(self.config) 

        #calling LLM factory
        self.llm = get_llm(self.config)

        #calling vectorstore factory
        self.vectorstore = get_vectorstore(self.config, self.embedding)

        #setting text splitter
        self.splitter = RecursiveCharacterTextSplitter(
            chunk_size = self.config["chunking"]["chunk_size"],
            chunk_overlap = self.config["chunking"]["chunk_overlap"]
        )

   
    def train(self,file_path:str):
        # Load document from loaders folder
        documents = load_document(file_path)  #uses loaders/document_loader.py
        
        #split into chunks
        chunks = self.splitter.split_documents(documents)

        #save to ChromoDB
        self.vectorstore.add_documents(chunks)

        return f"Successfully trained on {len(chunks)} chunks!"


    def ask(self, question:str):
        # Step 1 - Create retriever
        retriever = self.vectorstore.as_retriever( #as_retriever() converts the vector store into a Retriever object.
            search_kwargs={"k": 3} #search_kwargs={"k": 3} is a Python dictionary passed as an argument to configure how the retriever performs the search.
        )

        # Step 2 - Create prompt template
        prompt = ChatPromptTemplate.from_template("""
        Answer the question based only on the following context:
        {context}

        Question: {question}
        """)

        # Step 3 - Build chain
        chain = ( #A chain is a sequence of operations.
            {"context": retriever, "question": RunnablePassthrough()} #Receives the question and searches the vector database.
            | prompt #Simply passes the input unchanged.
            | self.llm #The prompt is sent to your LLM
            | StrOutputParser() #StrOutputParser() is a LangChain component that converts the LLM's output into a plain Python string.
        )

        # Step 4 - Return answer
        return chain.invoke(question)
    

    