import google.generativeai as genai
from typing import Dict

genai.configure(api_key="AIzaSyCtS-8mJgI872JJB1eA0v-UO6Fo380ktNY")
model = genai.GenerativeModel("gemini-1.5-flash")

def generate_ai_response(text: str, url: str) -> str:

    prompt = {
        "task": "job_listing_extraction",
        "language": "indonesian",
        "notes":
        """Extrak semua data informasi yang revelan dan dibutuhkan pelajari secara mendalam komponen-komponen yang ada pada website, dan kemudian berikan responsenya dalam bentuk JSON. Dengan ketentuan sebagai berikut : 
        
        1. Data yang di ambil tidak boleh di rubah maupun di tambahkan. Data yand di ambil harus bersifat [ORIGINAL]
        2. Jika tidak menemukan data untuk sebuah properti, masukkan tanda min (-) untuk data yang bernilai null
        3. Jika ada data yang berhubungan dengan nilai mata uang. Jika data tersebut memiliki garis datar (-), maka buat properti budgetnya menjadi sebuah objek yang memiliki properti bernama minimal_budget dan maksimal_budget dengan tipe data number. Jika ada data yang tidak memiliki garis datar. Maka isi dari properti budget adalah bertipe angka saja

        """,
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