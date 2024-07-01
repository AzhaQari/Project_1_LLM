import os
from langchain_openai import OpenAI

# Load API key from environment variable
api_key = os.getenv('OPENAI_API_KEY')

# Initialize the LLM object
llm = OpenAI(openai_api_key=api_key)

def get_response(message: str):
    response = llm.invoke(message)
    print(response)

# Example usage
if __name__ == "__main__":
    message = "Tell me something new you learned today in one sentence"
    get_response(message)
