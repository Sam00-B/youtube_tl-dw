# 🎥 YouTube TLDW (Too Long; Didn't Watch) Summarizer

An AI-powered web application that instantly generates concise, easy-to-read summaries of YouTube videos. By extracting video transcripts and processing them through Google's Gemini AI, this tool saves time and extracts key information from long-form content in seconds.

## ✨ Features
* **Instant Transcription:** Automatically extracts accurate transcripts directly from YouTube videos.
* **AI Summarization:** Utilizes the Google Gemini 2.5 Flash model to read transcripts and generate clear, structured summaries.
* **Hybrid Architecture:** Custom local-to-cloud setup designed to bypass YouTube's strict data center IP blocking.
* **Clean UI:** A lightweight, vanilla HTML/CSS/JS frontend for a seamless user experience.

## 🛠️ Tech Stack
* **Frontend:** HTML, CSS, Vanilla JavaScript (Hosted via GitHub Pages)
* **Backend:** Python, FastAPI, Uvicorn
* **APIs & Libraries:** `youtube-transcript-api`, `google-generativeai`, `python-dotenv`

---

## 📝 Project Architecture & Technical Decisions

### The Challenge: Cloud IP Blocking
During the deployment phase of this project, I encountered a common industry challenge: Google's strict anti-bot protections. Initially, the Python/FastAPI backend was fully deployed to a cloud server. However, YouTube actively monitors and blocks traffic coming from known data centers to prevent automated bots from scraping video data (resulting in `HTTP 429: Too Many Requests` or IP bans). 

### The Solution: A Hybrid "Local-to-Cloud" Architecture
Instead of paying for premium residential proxies to bypass the data center block, I engineered a hybrid architecture to keep the project 100% free while maintaining a public-facing UI:

* **Frontend (Cloud):** The frontend is deployed publicly and hosted via **GitHub Pages**. This provides a clean, accessible link for portfolio reviews.
* **Backend (Local):** The FastAPI Python server runs locally. When a user inputs a YouTube link on the live website, the frontend securely routes the API request to `localhost` (`127.0.0.1:8000`). 
* **The Result:** By running the backend locally, transcript requests are routed through a standard home Wi-Fi network (a residential IP). This completely bypasses YouTube's cloud-server blocks, successfully fetches the transcript, and passes the data to the Gemini API for summarization.

---

## 🚀 Getting Started (Local Setup)

Because the frontend requires the local backend to bypass YouTube's protections, you must run the local API server to use the application.

### Prerequisites
* Python 3.x installed
* A free [Google Gemini API Key](https://aistudio.google.com/app/apikey)

### Installation

### Installation

1. **Clone the repository:**
   ```bash
   git clone [https://github.com/Sam00-B/youtube_tl-dw.git](https://github.com/Sam00-B/youtube_tl-dw.git)
   cd youtube_tl-dw
2. **Install backend dependencies:**
   ```bash
   pip install -r requirements.txt
3.Set up your environment variables:
    Create a new file named .env in the root folder of the project.
    Add your Gemini API key to this file exactly like this:
    GEMINI_API_KEY=your_api_key_here
4. Usage
Start the local backend server:
Open your terminal, ensure you are in the youtube_tl-dw folder, and run:

Bash
uvicorn main:app --reload
Access the Frontend:

Option A (Local): Open your file explorer, locate the project folder, and double-click the index.html file to open it in your browser.

Option B (Live Link): Visit your public GitHub Pages link. (Note: Because the live HTTPS website is talking to your local HTTP server, your browser's security might block it. If the summary doesn't load, look for a shield icon or site settings in your browser's address bar and select "Allow insecure content" or "Load unsafe scripts").

Summarize! Paste a YouTube URL into the search bar, hit the button, and let the AI do the reading for you.
