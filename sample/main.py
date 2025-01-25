from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from scrape import (
    scrape_website,
    split_dom_content,
    clean_body_content,
    extract_body_content
)
import google.generativeai as genai

genai.configure(api_key="AIzaSyCtS-8mJgI872JJB1eA0v-UO6Fo380ktNY")
model = genai.GenerativeModel("gemini-1.5-flash")
app = FastAPI(title="AI Scraper Web")

class ScrapeRequest(BaseModel):
    url: str

class ParseRequest(BaseModel):
    description: str
    dom_content: str

@app.get("/")
def root():
    return {"message": "Welcome to the AI Scraper Web API"}

@app.post("/scrape/")
def scrape_site(request: ScrapeRequest):
    url = request.url
    if not url:
        raise HTTPException(status_code=400, detail="URL is required")

    try:
        result = scrape_website(url)
        body_content = extract_body_content(result)
        cleaned_content = clean_body_content(body_content)

        prompt = {
            "URL": url,
            "Data yang akan di proses": cleaned_content,
            "Tampilkan data ini menjadi lebih rapih dalam bentuk JSON, kelompokkan data-data yang ada pada website tersebut": "Data yang di ambil tidak boleh di rubah maupun di tambahkan. Data yand di ambil harus bersifat [ORIGINAL]",
            "Data yang di ambil": "Hanya data yang berkaitan dengan pekerjaan atau lowongan pekerjaan saja"
        }

        ai_response = model.generate_content(str(prompt))

        print(ai_response.text)



        return {"url": url, "dom_content": cleaned_content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))