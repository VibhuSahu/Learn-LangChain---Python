import os
from dotenv import load_dotenv
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace


load_dotenv()

def main():
    
    # Getting the Access Token From .env file
    token = os.getenv("ACCESS_TOKEN")
    
    # Check for Access Token
    if not token:
        raise ValueError("ACCESS_TOKEN is not set in .env")
    
    try:    
        llm = HuggingFaceEndpoint(
            repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            huggingfacehub_api_token=token,
            provider="featherless-ai",
            temperature=0.7,
            max_new_tokens=50
        )
        
        model = ChatHuggingFace(llm=llm)
        
        
        
        response = model.invoke("Explain what LangChain is in simple words.")
        
         
        print(f"\n{response.content}\n")
    
    except ValueError as e:
        print("\n[Configuration Error]")
        print(e)
    
    except Exception as e:
        print("\n[Runtime Error]")
        print(f"Error type: {type(e).__name__}")
        print(f"Error message: {e}")
    


if __name__ == "__main__":
    main()
