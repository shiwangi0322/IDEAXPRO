import requests
import os
from dotenv import load_dotenv

# 1. FIX: Get the absolute path to the directory where THIS file is
basedir = os.path.abspath(os.path.dirname(__file__))

# 2. FIX: Tell load_dotenv exactly where to find the .env file
load_dotenv(os.path.join(basedir, ".env"))

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")

# 3. FIX: Updated check to show you where the code looked if it fails
if not YOUTUBE_API_KEY:
    raise ValueError(f"YOUTUBE_API_KEY is missing. Looked in: {os.path.join(basedir, '.env')}")

def get_youtube_trending_videos(topic: str = "AI", region: str = "US"):
    url = "https://www.googleapis.com/youtube/v3/search"
    params = {
        "part": "snippet",
        "q": topic,
        "type": "video",
        "regionCode": region,
        "maxResults": 10,
        "order": "viewCount",
        "key": YOUTUBE_API_KEY,
    }
    
    try:
        response = requests.get(url, params=params)
        # 4. FIX: Added basic error handling to catch API-specific issues
        response.raise_for_status() 
        data = response.json()
        
        if "items" in data:
            return [
                {
                    "title": video["snippet"]["title"],
                    "url": f"https://www.youtube.com/watch?v={video['id']['videoId']}",
                }
                for video in data["items"]
            ]
    except Exception as e:
        print(f"YouTube API Error: {e}")
    
    return []