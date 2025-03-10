# https://www.alphavantage.co/

import os
from dotenv import load_dotenv
import pandas as pd
import json
import requests

load_dotenv()

# We use the same API_KEY as in the exercise ex_finance.py

api_key = os.getenv('FIN_API_KEY')


url = (
    f'https://www.alphavantage.co/query?'
    f'function=NEWS_SENTIMENT&'
    f'tickers=COIN,CRYPTO:BTC&'
    f'time_from=20250101T0101&'
    f'limit=15&'
    f'apikey={api_key}'
)

response = requests.get(url)

data = response.json()


# Extract relevant fields from the response
news_feed = data.get("feed", [])

# Prepare a list for storing structured data
cleaned_data = []

for article in news_feed:
    title = article.get("title", "N/A")
    url = article.get("url", "N/A")
    time_published = article.get("time_published", "N/A")
    source = article.get("source", "N/A")
    summary = article.get("summary", "N/A")
    sentiment_score = article.get("overall_sentiment_score", "N/A")
    sentiment_label = article.get("overall_sentiment_label", "N/A")
    
    # Extract tickers and their sentiment
    tickers = [
        f"{t.get('ticker', 'N/A')} ({t.get('ticker_sentiment_label', 'N/A')})"
        for t in article.get("ticker_sentiment", [])
    ]
    tickers = ", ".join(tickers) if tickers else "N/A"

    # Append cleaned data as a dictionary
    cleaned_data.append({
        "Title": title,
        "URL": url,
        "Published Time": time_published,
        "Source": source,
        "Summary": summary,
        "Sentiment Score": sentiment_score,
        "Sentiment Label": sentiment_label,
        "Tickers Mentioned": tickers
    })

# Convert list of dictionaries to a Pandas DataFrame
df = pd.DataFrame(cleaned_data)

print(df.head)

df.to_csv('./output/news.csv')
