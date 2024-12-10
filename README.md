# Web Content Extractor and Rewriter

This is a Streamlit-based web application that extracts and rewrites specific sections (like "Problem" and "The Gift") from a given webpage URL. The results, including the original and rewritten content, are displayed on the app and saved to a CSV file.

## Features

- Extracts specific sections (e.g., "Problem" and "The Gift") from the given URL.
- Rewrites the content while retaining the original meaning using OpenAI's GPT API.
- Saves the URL, original content, and rewritten content to a CSV file (`rewritten_descriptions.csv`).
- Provides an option to download the CSV file directly from the app.

## Prerequisites

1. Python 3.8 or higher
2. Install the required Python packages listed in `requirements.txt`.

## Installation and Usage

### Clone the Repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```
### Install Dependencies

Install the required Python libraries using pip:

```bash
pip install -r requirements.txt
```
### Add Your OpenAI API Key

Replace "your_openai_api_key" in app.py with your actual OpenAI API key.

### Run the Application

Run the Streamlit application using the following command:

```bash
streamlit run app.py
```
This will open the app in your default web browser. If it doesn’t open automatically, navigate to the URL displayed in your terminal (e.g., http://localhost:8501).

## Using the App

1. Enter a webpage URL in the text input box.
2. Click on **Submit**.
3. The app will:
   - Extract the "Problem" and "The Gift" sections from the URL.
   - Rewrite them using OpenAI GPT API.
   - Display both the original and rewritten content on the app.
4. The data will be saved to `rewritten_descriptions.csv` in the repository directory.
5. You can download the CSV file directly from the app using the download link.

---

## CSV File Format

The saved CSV file (`rewritten_descriptions.csv`) will have the following columns:

| URL | Original Problem | Original Gift | Modified Problem | Modified Gift |
|-----|------------------|---------------|------------------|---------------|

Each row corresponds to the input URL and its extracted and rewritten content.

---

## Example Output

Here’s an example row from the `rewritten_descriptions.csv`:

| URL                       | Original Problem                   | Original Gift                    | Modified Problem                  | Modified Gift                     |
|---------------------------|-------------------------------------|-----------------------------------|-----------------------------------|-----------------------------------|
| https://example.com/sample | "Sea turtles are endangered..."   | "Your donation helps save turtles..." | "Sea turtles face threats..."   | "Your support contributes to..." |
