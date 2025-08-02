from model_gen import generate_tournament_structures

# Example raw tournament text (simulating a scraped block)
raw_texts = [
    '''The National Chess Open 2025 will be held from September 10 to 12, 2025. This national-level event brings together top players from across the country. Visit https://nationalsports.in/chess for details. Watch live at https://youtube.com/chesslive. Image: https://cdn.example.com/images/chess2025.jpg''',
    '''International Youth Soccer Cup: August 20-30, 2025. International youth teams compete in a summer soccer showdown. More info at https://globalsoccer.com/youthcup. Streaming: https://twitch.tv/youthsoccer. Image: https://cdn.example.com/images/soccer2025.jpg'''
]

results = generate_tournament_structures(raw_texts)

for idx, tournament in enumerate(results, 1):
    print(f"\nTournament {idx}:")
    for k, v in tournament.items():
        print(f"  {k}: {v}")
