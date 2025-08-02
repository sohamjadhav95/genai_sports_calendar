import requests
from bs4 import BeautifulSoup
from typing import List

def scrape_tournament_urls() -> List[str]:
    # For demo: return a list of URLs to scrape
    return [
        "https://bookmysports.com/",
        "https://gotosport.in/",
        "https://eventyay.com/"
    ]

def scrape_raw_tournament_blocks(url: str) -> List[str]:
    # In production, parse tournament blocks from the HTML
    try:
        resp = requests.get(url, timeout=10)
        soup = BeautifulSoup(resp.text, 'html.parser')
        # This is a mock: in real use, parse actual blocks
        blocks = [soup.get_text()[:1000]]
        return blocks
    except Exception as e:
        print(f"Error scraping {url}: {e}")
        return []
