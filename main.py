from dotenv import load_dotenv
import asyncio


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
    
    
    
    


if __name__ == "__main__":
    # main()
    asyncio.run(customisingYourModel())
    
