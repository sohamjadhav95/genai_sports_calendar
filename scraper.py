import requests
from bs4 import BeautifulSoup
from typing import List

def scrape_tournament_urls() -> List[str]:
    # Updated for demo: use real/test URLs or static HTML blocks with event data
    # Example: Wikipedia sports events, ESPN, or static test pages
    return [
        'https://en.wikipedia.org/wiki/2024_Summer_Olympics',
        'https://en.wikipedia.org/wiki/2023_Cricket_World_Cup',
        'https://en.wikipedia.org/wiki/2022_FIFA_World_Cup',
        # Add more real or test URLs as needed
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
