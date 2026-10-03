import os
from dotenv import load_dotenv
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from sklearn.metrics.pairwise import cosine_similarity



def get_embeddings():
    
    api_key = os.getenv("GOOGLE_API_KEY")
    
    if not api_key:
        raise ValueError(
            "GOOGLE_API_KEY is not set. "
            "Please add it to your .env file. "
        )
    
    try:
        embeddings = GoogleGenerativeAIEmbeddings(
            model="models/gemini-embedding-001",
            google_api_key=api_key
        )
        return embeddings
    
    except Exception as e:
        raise RuntimeError(
            f"[Failed to initialize Gemini embeddings] \n{e}"
        )
    

def small_embedding_model():
    
    try:
        embeddings = get_embeddings()
        
        text = "LangChain is a framework for building applications with LLMs."
        
        if not text.split():
            raise(
                f"[Error] \nText cannot be empty."
            )
            
        vector = embeddings.embed_query(text)
        
        if not vector:
            raise(
                f"[Error] \nGemini returned an empty embedding."
            )
        
        print("Embedding Dimensions: ", len(vector))
        print(str(vector))
    
    except ValueError as e:
        raise(
            f"[Configuration Error] \n{e}"
        )
    
    except Exception as e:
        raise(
            f"[Embedding Error] \n{e}"
        )

def embed_multiple_documents():
    try:
        embeddings = get_embeddings()
        
        documents = [
            "LangChain is used to build LLM applications.", 
            "Python is a popular programming language.", 
            "Vector databases store embeddings."
        ]
        
        if not documents:
            raise(
                f"[Error] \nDocument list is empty."
            )
            
        vectors = embeddings.embed_documents(documents)
        
        if not vectors:
            raise(
                f"[Error] \nGemini returned empty embeddings."
            )
        
        print("Number o documents: ", len(vectors))
        print("Embedding dimensions: ", len(vectors[0]))
        
        for vector in vectors:
            print(str(vector))
    
    except ValueError as e:
        raise(
            f"[Configuration Error] \n{e}"
        )
    
    except Exception as e:
        raise(
            f"[Embedding Error] \n{e}"
        )


def compare_embeddings(user):
    try:
        if not user or not user.strip():
            raise(
                f"[Error] \nSearch query cannot be empty."
            )
        
        embeddings = get_embeddings()
        
        documents = [
            "LangChain is used to build LLM applications.", 
            "Python is a popular programming language.", 
            "Vector databases store embeddings."
        ]
        
        if not documents:
            raise(
                f"[Error] \nNo documents available for search."
            )
            
        documents = [
            document for document in documents
            if document and document.strip()
        ]
        
        if not documents:
            raise(
                f"[Error]\nNo valid documents available."
            )
        
        document_vectors = embeddings.embed_query(documents)
        
        if not document_vectors:
            raise(
                f"[Error] \nCould not generate document embeddings."
            )
        
        user_vector = embeddings.embed_query(user)
        
        if not user_vector:
            raise(
                f"[Error]\nCould not genrate query embedding."
            )
            
        scores = cosine_similarity(
            [user_vector],
            document_vectors
        )[0]
        
        if len(scores) == 0:
            raise(
                f"[Error]\nSimilarity calculation returned no results."
            )

        results = sorted(
            enumerate(scores),
            key=lambda x: x[1],
            reverse=True
        )
        
        index, score = results[0]
        
        print("\nSearch Query:")
        print(user)
        
        print('\nBest Match:')
        print(documents[index])
        
        print("\nSimilarity Score:")
        print(round(float(scores), 4))
        
        print("\nAll Results:")
        
        for index, score in results:
            print(f"{float(score):.4f} -> {documents[index]}")
        
    except ValueError as e:
        print(f'[Configuration Error]\n{e}')
        
    except Exception as e:
        print(f"[Search Error]\n{e}")
        

if __name__ == "__main__":
    # Test single embedding
    small_embedding_model()
    
    #Test multiple embeddings
    embed_multiple_documents()
    
    # Search
    compare_embeddings("Tell me about python")
