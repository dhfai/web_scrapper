import google.generativeai as genai
from typing import Dict

genai.configure(api_key="AIzaSyCtS-8mJgI872JJB1eA0v-UO6Fo380ktNY")
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_ai_response(text: str, url: str) -> str:

    prompt = {
        "task": "job_listing_extraction",
        "language": "indonesian",
        "notes": "Extrak semua data informasi yang revelan dan dibutuhkan pelajari secara mendalam komponen-komponen yang ada pada website, dan kemudian berikan responsenya dalam bentuk JSON",
        "data": {
            "text": text,
            "website_url": url
        },
        "parameters": {
            "entities": ["judul_pekerjaan", "deskripsi_pekerjaan", "tag_keahlian", "budget", "jangka_waktu", "persyaratan_pelamar"]
        }
    }
    try:
      ai_response = model.generate_content(str(prompt))
      print(ai_response.text)
      return ai_response.text
    except Exception as e:
        print(f"Error during AI response: {e}")
        return ""