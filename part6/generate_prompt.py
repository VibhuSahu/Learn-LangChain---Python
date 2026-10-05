from pathlib import Path
from langchain_core.prompts import PromptTemplate, load_prompt


def get_research_paper_prompt():
    try:
        prompt = PromptTemplate(
            template="""
                Please summarize the research paper titiled "{paper_input}"
                
                Explanation Style: {style_input}
                Explanation Length: {length_input}
                
                Requirements:
                1. Mathematical Details:
                    - Include relevant mathematical equations if present.
                    - Explain mathematical concepts using simple and intuitive example.
                2. Analogies:
                    - Use relatable analogies to simplify complex ideas.
                3. Accuracy:
                    - Do not guess or invent information.
                    - If certain information is not available in the paper, respond with:
                        "Insufficient informatin available"
                        
                Ensure the summary is clear, accurate and aligned with the provided style and length.
            """,
            input_variables=[
                "paper_input",
                "style_input",
                "length_input"
            ],
            validate_template=True
        )
        
        PROMPT_DIR = Path('prompts')
        PROMPT_FILE = PROMPT_DIR / 'research_paper.json'
        
        PROMPT_DIR.mkdir(
            parents=True,
            exist_ok=True
        )
        
        prompt.save(str(PROMPT_FILE))
        
        print(f"Prompt saved successfully: {PROMPT_FILE}")
        
    except PermissionError as e:
        raise PermissionError(
            "[Permission Error]\nPermission denied while saving the prompt."
        ) from e
    
    except OSError as e:
        raise OSError(
            f"[OS Error]\nFile system error while saving prompt: {e}"
        ) from e
    
    except RuntimeError as e:
        raise RuntimeError(f"[Runtime Error]\nPrompt creation error {e}") from e
    
    except Exception as e:
        raise RuntimeError(
            f"[Exception Error]\nUnexpected error while saving prompt: {e}"
        ) from e
        

def load_research_prompt():
    try:
        
        PROMPT_DIR = Path('prompts')
        PROMPT_FILE = PROMPT_DIR / 'research_paper.json'
        
        PROMPT_DIR.mkdir(
            parents=True,
            exist_ok=True
        )
        
        if not PROMPT_FILE.exists():
            raise FileNotFoundError(
                f"[FileNotFound Error]\nPrompt File does not exist: {PROMPT_FILE}"
            )
        
        prompt = load_prompt(
            str(PROMPT_FILE)
        )
        
        print("[Prompt loaded successfully.]")
        
        return prompt
    
    except FileNotFoundError as e:
        raise FileNotFoundError(
            f"[File Not Found]\nPrompt file was not found: {e}"
        ) from e

    except PermissionError as e:
        raise PermissionError(
            "[Permission Error]\nPermission denied while reading the prompt."
        ) from e
    
    except OSError as e:
        raise OSError(
            f"[OS Error]\nFile system error while loading prompt: {e}"
        ) from e
    
    except Exception as e:
        raise RuntimeError(
            f"[Unexpected Error]\nUnexpected Error while loading prompt: {e}"
        ) from e
        


        
