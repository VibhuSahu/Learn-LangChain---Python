import os
from langchain_huggingface import HuggingFaceEmbeddings
from sklearn.metrics.pairwise import cosine_similarity


def small_embedding_model():
    # Set Hugging Face cache directory
    # Models will be downloaded inside the current project's model folder
    os.environ["HF_HOME"] = os.path.join(os.getcwd(), "model")
    
    embeddings = HuggingFaceEmbeddings(
        model_name = "sentence-transformers/all-MiniLM-L6-v2"
    )
    
    text = "LangChain is a framework for building applications with LLMs."
    
    vector = embeddings.embed_query(text=text)
    
    print("Embedding demensions: ", len(vector))
    print(str(vector))


def embed_multiple_documents():
    # Set Hugging Face cache directory
    # Models will be downloaded inside the current project's model folder
    os.environ["HF_HOME"] = os.path.join(os.getcwd(), "model")
        
    
    embeddings = HuggingFaceEmbeddings(
        model_name = "sentence-transformers/all-MiniLM-L6-v2"
    )
    
    documents = [
        "LangChain is used to build LLM applications.",
        "Python is a popular programming language.",
        "Vector databases store embeddings."
    ]
    
    vector = embeddings.embed_documents(documents)
    
    
    print("Embedding demensions: ", len(vector))
    print(str(vector))
     

def compair_embeddings(user):
    os.environ["HF_HOME"] = os.path.join(os.getcwd(), "model")
    
    embeddings = HuggingFaceEmbeddings(
        model_name = "sentence-transformers/all-MiniLM-L6-v2"
    )
    
    documents = [
        "LangChain is used to build LLM applications.",
        "Python is a popular programming language.",
        "Vector databases store embeddings."
    ]
    
    vector = embeddings.embed_documents(documents)
    
    user_embeddings = embeddings.embed_query(user)
    
    scores = cosine_similarity([user_embeddings], vector)[0]
    
    
    index, score = sorted(list(enumerate(scores)), key=lambda x:x[1])[-1]
    
    print(documents[index])
    print("similarity score is: ", score)
    


if __name__ == "__main__":
    # small_embedding_model()
    
    # embed_multiple_documents()
    
    compair_embeddings("tell me about python")
