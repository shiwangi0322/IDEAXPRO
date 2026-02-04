# IDEAXPRO
AI-powered Streamlit application that generates YouTube video ideas using OpenAI API based on user-selected niche and audience.
🎥 IDEAXPRO
An AI-powered Streamlit web application that generates creative, niche-specific YouTube video ideas using the OpenAI API. The app helps content creators overcome creative blocks by instantly suggesting engaging video titles and hooks based on user input.

📌 Project Description (for GitHub)

The Ideaxpro is built using Python and Streamlit and leverages the OpenAI API to generate innovative YouTube video ideas. Users can provide details such as content niche and target audience, and the application returns multiple AI-generated video ideas in real time.

This project demonstrates the integration of AI APIs with Python-based web applications and is suitable for academic projects, hackathons, and personal portfolios.

✨ Features

🎯 Niche-based video idea generation

👥 Audience-specific suggestions

🤖 AI-powered content creation using OpenAI API

🖥️ Interactive UI built with Streamlit

⚡ Real-time responses

🧩 Simple and scalable Python codebase

🛠️ Tech Stack
Languages

Python

Frameworks & Libraries

Streamlit

OpenAI API

Tools

Conda

VS Code

Git & GitHub

📂 Project Structure
AI PROJECTS/
├── Backend/
│   ├── app.py
│   ├── requirements.txt
│   └── youtubetrends.py
├── README.md

📦 Installation & Setup
1️⃣ Clone the repository
git clone https://github.com/your-username/ai-youtube-video-idea-generator.git
cd ai-youtube-video-idea-generator

2️⃣ Create & activate conda environment
conda create --name ai_yt_idea_generator python=3.10 -y
conda activate ai_yt_idea_generator

3️⃣ Install dependencies
python -m pip install -r requirements.txt

▶️ Run the Application
streamlit run app.py


The app will open automatically in your browser.

🔐 Environment Variables

Create a .env file and add your OpenAI API key:

OPENAI_API_KEY=your_api_key_here

🧠 How It Works

User enters YouTube niche and target audience

Streamlit sends the input to the backend logic

OpenAI API generates video ideas

Results are displayed instantly in the UI

🌟 Use Cases

YouTube creators

Students learning AI & APIs

Hackathons & mini projects

Content marketing tools

🔮 Future Improvements

YouTube Trending API integration

SEO keyword generation

Multi-language support

Video description & tag generation

Dark/Light UI themes

📚 Learning Outcomes

Streamlit app development

API integration with Python

Prompt engineering basics

Environment & dependency management

Building real-world AI applications

