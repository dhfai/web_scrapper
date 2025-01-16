from fastapi import FastAPI, HTTPException
from models import ScrapeRequest
from scrape import scrape_website
from ai import generate_ai_response

app = FastAPI()

@app.post("/scrape")
async def scrape_and_extract(request: ScrapeRequest):
    url = request.url
    scraped_text = scrape_website(url)

    if not scraped_text:
         raise HTTPException(status_code=400, detail="Failed to scrape the website.")

    ai_response_text = generate_ai_response(scraped_text, url)

    if not ai_response_text:
       raise HTTPException(status_code=500, detail="Failed to generate AI response.")

    return {"extracted_data": ai_response_text}