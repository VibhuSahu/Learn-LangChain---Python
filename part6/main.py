import os
from generate_prompt import load_research_prompt
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from rich.markdown import Markdown
from rich.console import Console

def main(paper_input, style_input, length_input):
    try:
        console = Console()
        
        prompt = load_research_prompt()

        if prompt is None:
            raise ValueError("[Error]\nPrompt file is empty.")

        load_dotenv()
        api_key = os.getenv("GOOGLE_API_KEY")

        if not api_key:
            raise ValueError(
                "GOOGLE_API_KEY is missing."
                "\nAdd it to your .env file."
            )

        model = ChatGoogleGenerativeAI(
            model="gemini-2.5-flash-lite",
            google_api_key=api_key,
            temperature=0.3
        )

        prompt_value = prompt.invoke({
            "paper_input": paper_input,
            "style_input": style_input,
            "length_input": length_input
        })

        response = model.invoke(prompt_value)

        print("Gemini Response:")
        print("------------------------------------------------------------------------------------------------------------------------")
        console.print(Markdown(response.content))

    except ValueError as e:
        raise ValueError(f"[Value Error]\n{e}") from e

    except Exception as e:
        raise RuntimeError(f"[Unexpected Error]\n{e}") from e


if __name__ == "__main__":
    main(
        "Attention Is All You Need",
        "Beginner friendly",
        "Detailed"
    )
