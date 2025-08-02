import sqlite3
from typing import List, Dict, Any

DB_PATH = 'genai_sports_calendar.db'

def init_db():
    conn = sqlite3.connect(DB_PATH)
    with open('schema.sql', 'r') as f:
        conn.executescript(f.read())
    conn.commit()
    conn.close()

def insert_tournament(tournament: Dict[str, Any]):
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('''
        INSERT INTO tournaments (name, level, start_date, end_date, url, streaming_links, image_url, summary)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    ''', (
        tournament['name'],
        tournament['level'],
        tournament['start_date'],
        tournament['end_date'],
        tournament['url'],
        ','.join(tournament['streaming_links']),
        tournament['image_url'],
        tournament['summary']
    ))
    conn.commit()
    conn.close()

def get_all_tournaments() -> List[Dict[str, Any]]:
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('SELECT name, level, start_date, end_date, url, streaming_links, image_url, summary FROM tournaments')
    rows = cur.fetchall()
    conn.close()
    tournaments = []
    for row in rows:
        tournaments.append({
            'name': row[0],
            'level': row[1],
            'start_date': row[2],
            'end_date': row[3],
            'url': row[4],
            'streaming_links': row[5].split(',') if row[5] else [],
            'image_url': row[6],
            'summary': row[7],
        })
    return tournaments

def clear_all():
    conn = sqlite3.connect(DB_PATH)
    cur = conn.cursor()
    cur.execute('DELETE FROM tournaments')
    conn.commit()
    conn.close()
