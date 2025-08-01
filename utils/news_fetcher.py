import requests
import os
from dotenv import load_dotenv

load_dotenv()

def fetch_news(query):
    api_key = os.getenv("NEWS_API_KEY")
    if not api_key:
        return [{"title": "NEWS_API_KEY not set in .env file", "url": "#"}]

    url = f"https://newsapi.org/v2/everything?q={query}&apiKey={api_key}"
    response = requests.get(url)
    articles = response.json().get("articles", [])
    return [{"title": a["title"], "url": a["url"]} for a in articles[:5]]
