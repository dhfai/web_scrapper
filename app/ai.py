import google.generativeai as genai
from dotenv import load_dotenv
import os

load_dotenv()

API_KEY = os.getenv("GEMINI_API_KEY")

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_ai_response(text: str, url: str) -> str:

    prompt = {
        "taks": "judul_skripsi_fkip",
        "language": "indonesian",
        "notes":
        """
            Scrape semua data judul skripsi dari website https://digilib.unismuh.ac.id/fakultas/01/

            buat output datanya dalam bentuk file JSON dengan ketentuan sebagai berikut:
            1. Data yang diambil tidak boleh diubah maupun ditambah. Data yang diambil harus bersifat [ORIGINAL]
        """,
        "parameters": ["judul skripsi", "penulis", "nim"],
        "data": {
            "website_url": url,
            "judul": text,
        },
    }
    try:
      ai_response = model.generate_content(str(prompt))
      print(ai_response.text)
      return ai_response.text
    except Exception as e:
        print(f"Error during AI response: {e}")
        return ""