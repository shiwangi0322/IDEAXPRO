# 1. ALL IMPORTS MUST BE AT THE TOP
from fastapi import FastAPI, Query
from fastapi.middleware.cors import CORSMiddleware  # Added import
from google_trends import get_trending_keywords
from youtube_trends import get_youtube_trending_videos
from openai import OpenAI
import os
from dotenv import load_dotenv

# 2. LOAD ENVIRONMENT VARIABLES
load_dotenv()
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
openai = OpenAI(api_key=OPENAI_API_KEY)

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is missing. Check your .env file")

# 3. INITIALIZE THE APP
app = FastAPI()

# 4. CONFIGURE CORS MIDDLEWARE (Do this BEFORE defining routes)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],      # Permits Streamlit (Port 8501) to talk to FastAPI (Port 8000)
    allow_credentials=True,
    allow_methods=["*"],      # Allows all HTTP methods (GET, POST, etc.)
    allow_headers=["*"],      # Allows all headers
)

# 5. YOUR API ROUTES
@app.get("/generate_ideas/video")
def generate_video_ideas(
    topic: str = Query(..., title="Topic"),
    audience: str = Query("Beginners", title="Target Audience"),
    region: str = Query("US", title="Region"),
):
    # ... (Rest of your existing function code)
    # 1. Get trending keywords
    trending_keywords = get_trending_keywords(topic)
    if not trending_keywords:
        trending_keywords = ["No trending keywords found for this topic"]

    # 2. Get trending YouTube videos
    trending_videos = get_youtube_trending_videos(topic, region)
    if not trending_videos:
        trending_videos = [{"title": "No trending videos found", "url": "#"}]

    # 3. Generate video ideas using OpenAI
    prompt = f"""
    Generate 5 engaging YouTube video ideas on '{topic}' for '{audience}'.
    Consider these trending keywords: {', '.join(trending_keywords)}
    Use insights from these trending videos: {', '.join([video['title'] for video in trending_videos])}
    """

    try:
        response = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that generates YouTube video ideas."},
                {"role": "user", "content": prompt},
            ],
        )
        video_ideas = response.choices[0].message.content.strip()
    except Exception as e:
        video_ideas = f"OpenAI API error: {str(e)}"

    return {
        "trending_keywords": trending_keywords,
        "trending_videos": trending_videos,
        "video_ideas": video_ideas,
    }
