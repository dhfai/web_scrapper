from fastapi import FastAPI, HTTPException
from models import ScrapeRequest
from scrape import scrape_website
from ai import generate_ai_response

app = FastAPI()

@app.post("/scrape")
async def scrape_and_extract(request: ScrapeRequest):
    base_url = request.url
    print(f"Scraping and extracting data from {base_url} for {request.num_pages} pages.")
    results = []

    if request.num_pages < 1:
        scraped_text = scrape_website(base_url)
        print(f"Scraped text for {base_url}: {scraped_text}")
        if not scraped_text:
            raise HTTPException(status_code=400, detail=f"Failed to scrape the website at {base_url}.")

        ai_response_text = generate_ai_response(scraped_text, base_url)

        if not ai_response_text:
            raise HTTPException(status_code=500, detail=f"Failed to generate AI response for {base_url}.")

        results.append({"url": base_url, "extracted_data": ai_response_text})

    elif request.num_pages >= 1:
        for i in range(1, request.num_pages + 1):
            page_url = f"{base_url}{i}/"

            scraped_text = scrape_website(page_url)
            if not scraped_text:
                raise HTTPException(status_code=400, detail=f"Failed to scrape the website at {page_url}.")

            ai_response_text = generate_ai_response(scraped_text, page_url)
            if not ai_response_text:
                raise HTTPException(status_code=500, detail=f"Failed to generate AI response for {page_url}.")

            results.append({"url": page_url, "extracted_data": ai_response_text})

    return results
