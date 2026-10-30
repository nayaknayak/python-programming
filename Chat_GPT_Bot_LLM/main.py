import os
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")

client = genai.Client(api_key=api_key) if api_key else None


def get_client() -> genai.Client:
    """Return the Gemini client, initializing or raising a helpful error if API key is missing."""
    global client
    if client is None:
        key = os.getenv("GEMINI_API_KEY") or os.getenv("GOOGLE_API_KEY")
        if not key:
            raise ValueError(
                "Gemini API key not found. Please set GEMINI_API_KEY in your .env file."
            )
        client = genai.Client(api_key=key)
    return client


def ask_gemini(model: str = "gemini-2.5-flash", input: str = "") -> str:
    """Send a prompt to the specified Gemini model and return the text response."""
    current_client = get_client()
    response = current_client.models.generate_content(
        model=model,
        contents=input,
    )
    print(response)
    return response.text


# Backward compatibility alias
ask_gpt = ask_gemini


if __name__ == "__main__":
    if api_key:
        try:
            print("Listing available Gemini models:")
            for model in get_client().models.list():
                print(f"- {model.name} ({model.display_name})")
        except Exception as e:
            print(f"Error listing models: {e}")
    else:
        print("GEMINI_API_KEY is not set in your .env file.")
        print("Please add GEMINI_API_KEY=your_api_key in .env to use Gemini.")
