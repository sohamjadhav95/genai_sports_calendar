from fastapi import FastAPI
from database import get_all_tournaments, insert_tournament, clear_all
from pydantic import BaseModel
from typing import List
from scraper import scrape_tournament_urls, scrape_raw_tournament_blocks
from model_gen import generate_tournament_structures

app = FastAPI()

class Tournament(BaseModel):
    name: str
    level: str
    start_date: str
    end_date: str
    url: str
    streaming_links: List[str]
    image_url: str
    summary: str

@app.get("/tournaments", response_model=List[Tournament])
def get_tournaments():
    return get_all_tournaments()

@app.post("/refresh")
def refresh_tournaments():
    clear_all()
    urls = scrape_tournament_urls()
    for url in urls:
        blocks = scrape_raw_tournament_blocks(url)
        if not blocks:
            continue
        extracted = generate_tournament_structures(blocks)
        for tournament in extracted:
            # Only insert if required fields are present
            if tournament.get("name") and tournament.get("start_date"):
                insert_tournament(tournament)
    return {"status": "refreshed"}
