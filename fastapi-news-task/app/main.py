from fastapi import FastAPI,HTTPException
from .database import engine, Base, SessionLocal
from .models import News
from .news_fetcher import fetch_news
from .schemas import NewsOut
from datetime import datetime

Base.metadata.create_all(bind=engine)
app = FastAPI()


def parse_iso_datetime(dt_str: str) -> datetime:
    return datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%SZ")

@app.get("/")
def root():
    return {"message": "News API is Live!"}

@app.get("/fetch-news/", response_model=list[NewsOut])
def fetch_and_save():
    
    try :
        session = SessionLocal()
        articles = fetch_news()
        news_objects = []
        for article in articles:
            news = News(
            source_name=article.get("source", {}).get("name"),
            author=article.get("author"),
            title=article["title"],
            description=article.get("description"),
            url=article["url"],
            url_to_image=article.get("urlToImage"),
            content=article.get("content"),
            published_at=parse_iso_datetime(article["publishedAt"])
        )
        #     session.add(news)
            news_objects.append(news)
        # session.commit()
        # session.close()
        print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>',news_objects)
        return news_objects
    except Exception as e :
        raise HTTPException(status_code=500, detail=str(e))

