# GenAI Sports Tournament Calendar

## 🚀 How to Run

1. Install dependencies:
```bash
pip install -r requirements.txt
```

2. Initialize the database:
```bash
python -c "import database; database.init_db()"
```

3. Start the server:
```bash
uvicorn main:app --reload
```

4. Visit http://127.0.0.1:8000/tournaments to fetch data.

## 🧠 What It Does
- Scrapes tournaments across multiple sports.
- Uses Groq LLM (Gemma-2-9b-it) to extract structured info.
- Serves data via FastAPI API.
- (Planned) Streamlit UI for demo purposes.

## 🛠 Structure
- `scraper.py`: Raw data collection
- `model_gen.py`: GenAI text → structured data (via Groq LLM)
- `database.py`: Insert/fetch tournaments
- `main.py`: API
- `templates/`: (Optional) UI display
- `data/sample_output.json`: Sample tournaments

## 🏁 Execution Notes
- Requires Groq API key for extraction (set in `model_gen.py`).
- Add new tournaments by scraping or manually inserting using the database module.

---

## Example Tournament JSON
See `data/sample_output.json` for 5 sample tournaments.
