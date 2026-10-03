import os

from dotenv import load_dotenv
from langchain_huggingface import ChatHuggingFace, HuggingFacePipeline


load_dotenv()


def main():
    
    try:    
        # Set Hugging Face cache directory
        # Store Hugging Face downloaded models in the current project directory
        os.environ["HF_HOME"] = os.path.join(os.getcwd(), "model")
        
        
        # Creating Pipeline
        llm = HuggingFacePipeline.from_model_id(
            model_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
            task='text-generation',
            pipeline_kwargs = dict(
                temperature=0.5,
                max_new_tokens=100
            )
        )
        
        # Convert HuggingFacePipline into a Chat Model.
        model = ChatHuggingFace(llm=llm)
        
        
        # Sending a prompt to the model
        response = model.invoke("Who is Iron Man?")
        
        
        # Display the response
        print(response.content)

    except OSError as error:
        print("\n[File or model loading problem]")
        print(f"Details: {error}")    
        
        print(
            "\nPossible causes:"
            "\n1. Insufficient disk space."
            "\n2. Model download was interrupted."
            "\n3. Hugging Face cache directory is not writable."
            "\n4. Required model files are missing."
        )
        
        
    except ImportError as error:
        print("\n[Required Python package is missing.]")
        print(f"Details: {error}")   
        
        print(
            "\nInstall the required packages using:"
            "\nuv add langchain langchain-huggingface transformers torch python-dotenv"
            )
    
    except Exception as error:
        print("\n[An Unexpected Error Occurred]")
        print(f"Error type: {type(error).__name__}")
        print(f"Details: {error}")
        


if __name__ == "__main__":
    main()
