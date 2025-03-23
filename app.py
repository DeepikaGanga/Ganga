import streamlit as st
import requests
import pandas as pd
from gtts import gTTS
import os
import playsound

st.title("Company News Sentiment Analysis")
company_name = st.text_input("Enter the company name:")

if st.button("Fetch News"):
    response = requests.get(f'http://127.0.0.1:5000/api/news?company={company_name}')
    
    if response.status_code != 200:
        st.error(f"Error fetching news: {response.status_code} - {response.text}")
    else:
        try:
            articles = response.json()
            if articles and isinstance(articles, list):  # Check for valid response
                df = pd.DataFrame(articles)

                st.subheader("News Articles")
                st.dataframe(df)

                # Comparative Analysis
                average_polarity = df['polarity'].mean()
                average_subjectivity = df['subjectivity'].mean()

                st.write(f"\n**Average Polarity:** {average_polarity:.4f}")
                st.write(f"**Average Subjectivity:** {average_subjectivity:.4f}")

                # Convert summaries to Hindi speech
                summaries = " ".join(df['summary'].tolist())
                tts = gTTS(text=summaries, lang='hi')
                filename = "summary.mp3"
                tts.save(filename)

                # Provide an option to play audio
                if st.button("Play Summary Audio"):
                    playsound.playsound(filename)
                    os.remove(filename)  # Remove the file after playing
            else:
                st.warning("No articles to display or error fetching news.")
        except ValueError:
            st.error("Error decoding JSON response.")
