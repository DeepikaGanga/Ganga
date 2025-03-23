from flask import Flask, request, jsonify
import requests
from textblob import TextBlob
import pandas as pd

app = Flask(__name__)

def fetch_and_analyze_news(company_name):
    url = f'https://newsapi.org/v2/everything?q={company_name}&apiKey=8d3ffe25b3a5465297712cab808faf91&pageSize=10&language=en'
    
    response = requests.get(url)
    
    if response.status_code != 200:
        return {"error": f"Error fetching news: {response.status_code}"}

    articles = response.json().get('articles', [])
    extracted_articles = []

    for article in articles:
        title = article.get('title')
        summary = article.get('description') or 'No Summary'
        url = article.get('url')
        published_at = article.get('publishedAt')
        source = article.get('source', {}).get('name')

        # Perform sentiment analysis
        text = f"{title} {summary}"
        blob = TextBlob(text)
        polarity = blob.sentiment.polarity
        subjectivity = blob.sentiment.subjectivity

        # Determine sentiment category
        sentiment = 'Positive' if polarity > 0 else 'Negative' if polarity < 0 else 'Neutral'

        # Store article information and sentiment
        extracted_articles.append({
            'title': title,
            'summary': summary,
            'url': url,
            'published_at': published_at,
            'source': source,
            'polarity': polarity,
            'subjectivity': subjectivity,
            'sentiment': sentiment
        })

    return extracted_articles  # Return the list directly

@app.route('/api/news', methods=['GET'])
def get_news():
    company_name = request.args.get('company')
    articles = fetch_and_analyze_news(company_name)
    return jsonify(articles)  # This will now return a list

if __name__ == '__main__':
    app.run(debug=True)
