from groq import Groq
from typing import List, Dict

GROQ_API_KEY = "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"

PROMPT_TEMPLATE = '''Extract this text into the following JSON format:\n{{\n  "name": "",
  "level": "",
  "start_date": "",
  "end_date": "",
  "url": "",
  "streaming_links": [],
  "image_url": "",
  "summary": ""\n}}\nText: {text}'''

def generate_tournament_structures(texts: List[str]) -> List[Dict]:
    client = Groq(api_key=GROQ_API_KEY)
    results = []
    for text in texts:
        prompt = PROMPT_TEMPLATE.format(text=text)
        completion = client.chat.completions.create(
            model="llama-3.1-8b-instant",
            messages=[{"role": "user", "content": prompt}],
            temperature=1,
            top_p=1,
            stream=True,
            stop=None,
        )
        response_content = ""
        for chunk in completion:
            response_content += chunk.choices[0].delta.content or ""
        import json
        import re
        try:
            # Try to extract JSON from code block or plain text
            match = re.search(r'```json\s*({[\s\S]*?})\s*```', response_content)
            if not match:
                match = re.search(r'({[\s\S]*})', response_content)
            if match:
                json_str = match.group(1)
                data = json.loads(json_str)
                results.append(data)
            else:
                print(f"Could not find JSON in response. Raw response: {response_content}")
        except Exception as e:
            print(f"Extraction error: {e}\nRaw response: {response_content}")
    return results
