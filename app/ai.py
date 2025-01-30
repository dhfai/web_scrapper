import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

if not API_KEY:
    raise ValueError("❌ API key for Gemini is missing. Please set GEMINI_API_KEY in your .env file.")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_ai_response(text: str, url: str, task: str, parameters: list) -> str:
    """
    Generate AI response dynamically based on user-defined task and parameters.

    Args:
        text (str): Scraped text content from the website.
        url (str): Website URL being scraped.
        task (str): Task description for AI
        parameters (list): List of data parameters to extract.

    Returns:
        str: AI-generated response or empty string if an error occurs.
    """
    prompt = {
        "task": task,
        "language": "indonesian",
        "notes": f"""
            Scrape semua data dari website {url}

            Buat output dalam format JSON dengan ketentuan sebagai berikut:
            ***Data yang diambil tidak boleh diubah maupun ditambah. Data harus bersifat [ORIGINAL]***
        """,
        "parameters": parameters,
        "data": {
            "website_url": url,
            "extracted_text": text,
        },
    }

    try:
        print(f"🚀 Sending request to Gemini AI with task: {task}")
        ai_response = model.generate_content(str(prompt))

        if ai_response and hasattr(ai_response, 'text'):
            print(f"✅ AI Response received: {ai_response.text}...")
            return ai_response.text
        else:
            print("❌ AI response is empty or invalid.")
            return ""
    except Exception as e:
        print(f"❌ Error during AI response generation: {e}")
        return ""
