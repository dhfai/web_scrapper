import requests
from bs4 import BeautifulSoup

def scrape_website(url: str) -> str:

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text(separator=' ', strip=True)
        return text
    except requests.exceptions.RequestException as e:
        print(f"Error during scraping: {e}")
        return ""