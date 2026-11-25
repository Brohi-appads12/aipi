import json
import urllib.request
from datetime import datetime

url = "https://api.sofascore.com/api/v1/sport/football/events/live"
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36",
    "Accept": "application/json",
    "Referer": "https://www.sofascore.com/"
}

req = urllib.request.Request(url, headers=headers)

try:
    with urllib.request.urlopen(req, timeout=15) as response:
        data = json.loads(response.read().decode("utf-8"))
        events = data.get("events", [])
        print(f"Total live matches milay: {len(events)}")

        with open("matches.json", "w", encoding="utf-8") as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
        print("matches.json save ho gayi!")

except Exception as e:
    print(f"Error aaya: {e}")
    exit(1)
