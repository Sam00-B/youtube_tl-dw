from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from youtube_transcript_api import YouTubeTranscriptApi
import google.generativeai as genai
import re
import os
from dotenv import load_dotenv
load_dotenv()
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)
my_key=os.getenv("GEMINI_API_KEY")
if not my_key:
    raise ValueError("GEMINI_API_KEY not found in environment variables")
genai.configure(api_key=my_key)
model = genai.GenerativeModel('gemini-2.5-flash')
def get_video_id(url):
    match = re.search(r"(?:v=|\/)([0-9A-Za-z_-]{11}).*", url)
    return match.group(1) if match else None
@app.get("/summarize")
async def summarize_video(url: str):
    video_id = get_video_id(url)
    if not video_id:
        raise HTTPException(status_code=400, detail="Invalid YouTube URL")
    try:
        # 1. Get the transcript for the video
        api=YouTubeTranscriptApi()
        transcript_data = api.fetch(video_id).to_raw_data()
        transcript_text = " ".join([d['text'] for d in transcript_data])
        
        # 2. safety limit for ai
        transcript_text = transcript_text[:15000] 

        # 3. Create the prompt for the AI
        prompt = f"""
    Analyze this YouTube transcript and provide a detailed response in plain text.

    Rules:

    Do not use markdown symbols like #, *, or ---
    Write in clean readable paragraphs
    Avoid vague or generic summaries
    Explain the main arguments, context, and conclusions clearly

    Include:
    Detailed Summary:
    Explain the main discussion, arguments, and overall message.

    Key Takeaways:
    Write clear points with explanations and examples from the transcript.

    Important Statements:
    List notable quotes or major claims from the speaker.

    Transcript:{transcript_text}
        """

        # 4. Ask the AI and return the response
        response = model.generate_content(prompt)
        return {"summary": response.text}

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))