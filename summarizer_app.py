import streamlit as st
import requests
from bs4 import BeautifulSoup
import google.generativeai as genai

# Configure Google Gemini API
GOOGLE_API_KEY = "abcd"
genai.configure(api_key=GOOGLE_API_KEY)

# Function to extract text from a webpage
def extract_text_from_url(url):
    try:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract text from paragraph tags
        paragraphs = soup.find_all("p")
        text = "\n".join([p.get_text() for p in paragraphs])

        return text if text else "No readable content found."
    except Exception as e:
        return f"Error extracting text: {e}"

# Function to summarize text using Google Gemini API
def summarize_text(text):
    try:
        model = genai.GenerativeModel("gemini-1.5-pro-latest")  # Choose a fast or detailed model
        response = model.generate_content(text)
        return response.text
    except Exception as e:
        return f"Error summarizing text: {e}"

# Streamlit UI
st.set_page_config(page_title="Web Page Summarizer", layout="wide")
st.title("📄 Web Page Summarizer")
st.write("Enter a URL, and this tool will extract and summarize the webpage content using Google Gemini AI.")

# User Input
url = st.text_input("🔗 Enter Website URL:", placeholder="https://example.com")

if st.button("Summarize"):
    with st.spinner("Extracting text..."):
        extracted_text = extract_text_from_url(url)
    
    with st.spinner("Generating summary..."):
        summary = summarize_text(extracted_text)

    # Display results
    st.subheader("📜 Extracted Text")
    st.write(extracted_text[:2000] + "...")  # Limit output to avoid clutter

    st.subheader("📝 Summary")
    st.write(summary)
