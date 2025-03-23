# News Summarization

## Description
This project fetches news articles related to a specified company, performs sentiment analysis, and summarizes the results. It features a web-based interface built with Streamlit, allowing users to input a company name and retrieve relevant news articles.

## Requirements
- Python 3.x
- Flask
- Streamlit
- Requests
- TextBlob
- pandas
- gTTS
- playsound

## Setup Instructions
1. Install Dependencies present in requirements.txt file.
2. Get an API Key:
Sign up for a free API key at News API.
Replace the placeholder API key in api.py with your actual key.
3. Open a split terminal:
Run 'python api.py' on one terminal.
Run 'python -m streamlit run app.py' or 'streamlit run app.py' on another terminal.

## Usage Instructions
- Once you run the above commands in terminals, you'll be redirected to streamlit app in your browser.
- Enter the name of the company you want to fetch news for in the input field
- Click the "Fetch News" button to retrieve articles.
- View the summarized articles and their sentiment analysis results.
- Click "Play Summary Audio" to listen to the Hindi speech of the summarized content.