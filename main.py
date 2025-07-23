import os
from dotenv import load_dotenv
from google import genai
import sys
from google.genai import types


def main():
    load_dotenv()
    api_key = os.environ.get("GEMINI_API_KEY")

    args = sys.argv[1:]

    if not args:
        print("No prompt was given")
        sys.exit(1)

    if args[-1] == "--verbose":
        user_prompt = " ".join(args[:-1])
        print(f"User prompt: {user_prompt}")

    else:
        user_prompt = " ".join(args)

    messages = [types.Content(role="user", parts=[types.Part(text=user_prompt)])]

    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
    model="gemini-2.0-flash-001", contents=messages,    
)
    if args[-1] == "--verbose":
        print(f"Prompt tokens: {response.usage_metadata.prompt_token_count}")
        print(f"Response tokens: {response.usage_metadata.candidates_token_count}") 
    print("Response:")
    print(response.text)
    


if __name__ == "__main__":
    main()
