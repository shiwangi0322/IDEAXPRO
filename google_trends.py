
# google_trends.py
import requests
import os
from dotenv import load_dotenv

# Use an absolute path so it always finds the .env file in this folder
basedir = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(basedir, '.env'))

# Make sure this variable name matches your .env file
SERPAPI_KEY = os.getenv("SERPAPI_API_KEY")

if not SERPAPI_KEY:
    raise ValueError(f"SERPAPI_API_KEY is missing. Looked in: {os.path.join(basedir, '.env')}")

def get_trending_keywords(topic: str = "artificial intelligence"):
    url = "https://serpapi.com/search.json"
    params = {
        "engine": "google_trends",
        "q": topic,
        "hl": "en",
        "date": "today 12-m",
        "tz": "420",
        "data_type": "trends",
        "api_key": SERPAPI_KEY,
    }
    
    response = requests.get(url, params=params)
    data = response.json()
    
    if "related_queries" in data and data["related_queries"].get("top"):
        keywords = [
            item["query"] for item in data["related_queries"]["top"]
            if "ai" in item["query"].lower() or "artificial intelligence" in item["query"].lower()
        ]
        return keywords[:10]
    
    return []