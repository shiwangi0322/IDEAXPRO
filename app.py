import streamlit as st

import requests

# Backend API URL
API_URL = "http://localhost:8000/generate_ideas/video"

st.title("AI-POWERED YouTube Video Idea Generator")

# Input fields for topic, audience, and region
topic = st.text_input("Enter the topic for video ideas:", "Artificial Intelligence")
audience = st.selectbox("Enter the target audience:", ["Tech Enthusiasts", "Beginners", "Professionals"])
region = st.text_input("YouTube region code (e.g., US, IN):", "US")

# Submit button
if st.button("Generate Video Ideas"):
    params = {
        "topic": topic,
        "audience": audience,
        "region": region,
    }
    
    try:
        response = requests.get(API_URL, params=params)
        
        if response.status_code == 200:
            data = response.json()
            
            # Trending Keywords
            st.subheader("Trending Keywords:")
            if data.get("trending_keywords"):
                st.write(", ".join(data["trending_keywords"]))
            else:
                st.write("No trending keywords found.")
                
            # Trending Videos
            st.subheader("Trending YouTube Videos:")
            if data.get("trending_videos"):
                for video in data["trending_videos"]:
                    st.markdown(f"- [{video['title']}]({video['url']})")
            else:
                st.write("No trending videos found.")
                
            # AI-Generated Video Ideas
            st.subheader("AI-Generated Video Ideas:")
            # Logic check for the specific error string or empty content
            if "OpenAI API error" in str(data.get("video_ideas", "")):
                st.error(data["video_ideas"])
            else:
                st.write(data.get("video_ideas", "No ideas generated."))
        else:
            st.error(f"Failed to fetch data. Status code: {response.status_code}")
            
    except requests.exceptions.RequestException as e:
        st.error(f"Connection Error: {e}")
        

