🧠 Webpage Summarizer using Gemini API

Transform long webpages into crisp, AI-generated summaries using Google’s Gemini large language model — all in Python 🐍.
Just paste a URL, and get a clean, context-aware summary in seconds.

🚀 Features

✅ Extracts full text content from any webpage
✅ Uses Gemini API to generate concise summaries
✅ Handles long and messy pages gracefully
✅ Clean and modular Python codebase
✅ Supports command-line and web interface (optional with Streamlit/Flask)

🧩 Tech Stack
Component	Technology
Programming Language	Python 3.x
AI Model	Google Gemini API (Generative AI)
Web Scraping	requests, BeautifulSoup4
Environment	.env for API key management
(Optional Frontend)	Streamlit or Flask for UI
📦 Installation
# 1️⃣ Clone this repository
git clone https://github.com/aryan-trivedi/web-page-summarizer.git
cd web-page-summarizer
# 2️⃣ Create a virtual environment (recommended)
python -m venv venv
source venv/bin/activate   # (Linux/Mac)
venv\Scripts\activate      # (Windows)

# 3️⃣ Install dependencies
pip install -r requirements.txt

# 4️⃣ Set your Gemini API Key
# Create a .env file in the root directory and add:
GEMINI_API_KEY=your_api_key_here

🧠 Usage
🖥️ Command-Line Version
python summarize.py "https://example.com/article"


Output:

🔗 URL: https://example.com/article
📝 Summary:
This article discusses how machine learning models like Gemini can summarize complex text...

🌐 Optional: Run with Streamlit UI
streamlit run app.py


Then open the local server URL (e.g., http://localhost:8501) and paste a webpage link to get instant summaries.

⚙️ Code Overview

summarize.py

import os
import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv
from google import genai

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
model = genai.GenerativeModel("gemini-1.5-pro")

def extract_text_from_url(url):
    html = requests.get(url).text
    soup = BeautifulSoup(html, "html.parser")
    return " ".join([p.get_text() for p in soup.find_all("p")])

def summarize_webpage(url):
    text = extract_text_from_url(url)
    prompt = f"Summarize the following webpage content clearly and concisely:\n\n{text}"
    response = model.generate_content(prompt)
    return response.text

if __name__ == "__main__":
    import sys
    print("🔗 URL:", sys.argv[1])
    print("📝 Summary:\n", summarize_webpage(sys.argv[1]))

🧾 Example Output

Input URL:
https://www.bbc.com/news/technology-123456

Generated Summary:

The article explains recent advances in generative AI models, focusing on Gemini’s multimodal abilities and its comparison with GPT models...

🔒 Environment Variables
Variable	Description
GEMINI_API_KEY	Your Google Gemini API key from Google AI Studio


📈 Future Enhancements

 Support PDF / TXT file summarization

 Add keyword extraction

 Browser extension version

 Support multilingual summaries

 Integrate caching for faster results

🤝 Contributing

Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to improve.

📜 License

This project is licensed under the MIT License — free for personal and commercial use.

⭐ Show Your Support

If you found this useful, give it a ⭐ on GitHub
 — it helps others discover it!
