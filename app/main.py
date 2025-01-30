from fastapi import FastAPI, HTTPException
from models import ScrapeRequest
from scrape import scrape_website
from ai import generate_ai_response

app = FastAPI()

@app.post("/scrape")
async def scrape_and_extract(request: ScrapeRequest):
    """
    Scrape website and extract AI-processed data.

    Args:
        request (ScrapeRequest): JSON payload with `url`, `num_pages`, `task`, and `parameters`.

    Returns:
        List[Dict]: List of extracted data for each page.
    """
    base_url = request.url
    task = request.task
    parameters = request.parameters
    results = []

    print(f"🌐 Scraping data from {base_url} for {request.num_pages} pages with task: {task}")

    for i in range(1, max(1, request.num_pages) + 1):
        page_url = base_url if request.num_pages == 0 else f"{base_url}{i}/"

        print(f"🔍 Processing {page_url}...")

        scraped_text = scrape_website(page_url)
        if not scraped_text:
            raise HTTPException(status_code=400, detail=f"❌ Failed to scrape the website at {page_url}.")

        ai_response_text = generate_ai_response(scraped_text, page_url, task, parameters)
        if not ai_response_text:
            raise HTTPException(status_code=500, detail=f"❌ Failed to generate AI response for {page_url}.")

        results.append({"url": page_url, "extracted_data": ai_response_text})

    return results
