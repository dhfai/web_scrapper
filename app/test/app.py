# import requests
# from bs4 import BeautifulSoup
# import google.generativeai as genai

# genai.configure(api_key="AIzaSyCtS-8mJgI872JJB1eA0v-UO6Fo380ktNY")
# model = genai.GenerativeModel("gemini-1.5-flash")

# def scrape_website(url):
#     response = requests.get(url)
#     soup = BeautifulSoup(response.content, 'html.parser')

#     text = soup.get_text()


#     prompt = {
#         "task": "job_listing_extraction",
#         "language": "indonesian",
#         "data": {
#             "text": text,
#             "website_url": url
#         },
#         "parameters": {
#             "entities": ["judul_pekerjaan", "deskripsi_pekerjaan", "tag_keahlian", "budget", "jangka_waktu", "persyaratan_pelamar"]
#         }
#     }

#     ai_response = model.generate_content(str(prompt))

#     print(ai_response.text)
#     return ai_response.text

# url = 'https://projects.co.id/public/browse_projects/listing'
# scraped_data = scrape_website(url)







from fastapi import FastAPI
from pydantic import BaseModel
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

genai.configure(api_key="AIzaSyCtS-8mJgI872JJB1eA0v-UO6Fo380ktNY")
model = genai.GenerativeModel("gemini-1.5-flash")

app = FastAPI()

class ScrapeRequest(BaseModel):
    url: str

@app.post("/scrape")
async def scrape_website(request: ScrapeRequest):
    url = request.url
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')
    text = soup.get_text()

    prompt = {
        "task": "job_listing_extraction",
        "language": "indonesian",
        "notes": "Extract all relevant information from a job listing and give the response json format.",
        "data": {
            "text": text,
            "website_url": url
        },
        "parameters": {
            "entities": ["judul_pekerjaan", "deskripsi_pekerjaan", "tag_keahlian", "budget", "jangka_waktu", "persyaratan_pelamar"]
        }
    }

    ai_response = model.generate_content(str(prompt))
    print(ai_response.text)
    return {"extracted_data": ai_response.text}

