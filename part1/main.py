from dotenv import load_dotenv
import asyncio
import os


load_dotenv()

async def main():
    from langchain.chat_models import init_chat_model
    
    chat = init_chat_model(model="google_genai:gemini-2.5-flash-lite")
    
    print(chat.invoke("How are you"))
    
async def customisingYourModel():
    from langchain.chat_models import init_chat_model
    
    chat = init_chat_model(
        model="google_genai:gemini-2.5-flash-lite",
        # Kwargs passed to the model:
        temperature=1.0
    )
    
    print(list(chat.invoke("What's the capital of the Moon?"))[0][1])
    
    
def LLM_demo():
    from google import genai
    
    token = os.getenv("GOOGLE_API_KEY")
    
    if not token:
        raise ValueError("There is no API KEY")
    
    client = genai.Client(
        api_key=token
    )
    
    response = client.models.generate_content(
        model="gemini-2.5-flash-lite",
        contents="Explain LangChain in simple words",
        config={
            'max_output_tokens': 100
        }
    )
    
    print(response.text)


if __name__ == "__main__":
    # main()
    # asyncio.run(customisingYourModel())
    LLM_demo()
    
