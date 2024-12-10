import streamlit as st
import requests
from bs4 import BeautifulSoup
from openai import OpenAI
import pandas as pd
import os

# Initialize the OpenAI client with your API key
client = OpenAI(api_key="")

# CSV file path
CSV_FILE = "rewritten_descriptions.csv"

def fetch_content(url):
    """Fetch and parse the content from the provided URL."""
    try:
        response = requests.get(url)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        
        # Locate "Problem" and "The Gift" sections based on the HTML structure
        problem_header = soup.find("h4", string=lambda x: x and "Problem" in x)
        gift_header = soup.find("h4", string=lambda x: x and "The Gift" in x)
        
        problem_text = problem_header.find_next("p").text if problem_header else "Problem section not found."
        gift_text = gift_header.find_next("p").text if gift_header else "The Gift section not found."
        
        return problem_text, gift_text
    except Exception as e:
        st.error(f"Error fetching content: {e}")
        return None, None

def rewrite_text_with_chat(text):
    """Rewrite the given text using OpenAI Chat API."""
    try:
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that rewrites text while retaining its original meaning."},
                {"role": "user", "content": f"Rewrite the following text to retain its meaning but make it slightly different:\n\n{text}"}
            ]
        )
        # Extract the content from the API response
        rewritten_text = response.choices[0].message.content.strip()
        return rewritten_text
    except Exception as e:
        st.error(f"Error rewriting text: {e}")
        return "Error in rewriting."

def save_to_csv(data, file_path):
    """Save the data to a CSV file."""
    # Check if the file exists
    if not os.path.exists(file_path):
        # Create a new file with headers if it doesn't exist
        df = pd.DataFrame(data, columns=["URL", "Original Problem", "Original Gift", "Modified Problem", "Modified Gift"])
        df.to_csv(file_path, index=False)
    else:
        # Append to the existing file
        df = pd.DataFrame(data, columns=["URL", "Original Problem", "Original Gift", "Modified Problem", "Modified Gift"])
        df.to_csv(file_path, mode='a', header=False, index=False)

# Streamlit application
st.title("Web Content Extractor and Rewriter")
st.markdown("Enter a URL, and the app will extract and rewrite 'Problem' and 'The Gift' sections. Results will be saved to a CSV file.")

# Input URL
url = st.text_input("Enter the URL", placeholder="https://example.com")

if url:
    with st.spinner("Fetching content..."):
        problem, gift = fetch_content(url)
    
    if problem and gift:
        st.subheader("Original Content")
        st.markdown("### Problem")
        st.write(problem)
        st.markdown("### The Gift")
        st.write(gift)
        
        with st.spinner("Rewriting content..."):
            rewritten_problem = rewrite_text_with_chat(problem)
            rewritten_gift = rewrite_text_with_chat(gift)
        
        st.subheader("Rewritten Content")
        st.markdown("### Problem")
        st.write(rewritten_problem)
        st.markdown("### The Gift")
        st.write(rewritten_gift)

        # Save to CSV
        save_data = [[url, problem, gift, rewritten_problem, rewritten_gift]]
        save_to_csv(save_data, CSV_FILE)
        st.success(f"Data saved to {CSV_FILE}")

        # Option to download the CSV file
        st.markdown(f"[Download the CSV file](./{CSV_FILE})")
