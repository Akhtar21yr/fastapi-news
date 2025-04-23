import requests
from .config import settings

def fetch_news():
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={settings.NEWS_API_KEY}"
    res = requests.get(url)
    print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',res.json().get("articles", []))
    return res.json().get("articles", [])
