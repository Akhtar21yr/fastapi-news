from celery import Celery
from celery.schedules import crontab
from .config import settings
from .news_fetcher import fetch_news
from .database import SessionLocal
from .models import News
from datetime import datetime

def parse_iso_datetime(dt_str: str) -> datetime:
    return datetime.strptime(dt_str, "%Y-%m-%dT%H:%M:%SZ")

celery_app = Celery(
    "worker",
    broker=settings.REDIS_BROKER,
    backend=settings.REDIS_BROKER,
    include=["app.celery_worker"]
)

celery_app.conf.beat_schedule = {
    "fetch-news-every-minute": {
        "task": "app.celery_worker.fetch_news_task",
        "schedule": crontab(minute="*"),  
    },
}
celery_app.conf.timezone = "UTC" 

@celery_app.task
def fetch_news_task():
    db = SessionLocal()
    articles = fetch_news()
    news_list = []

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
        news_list.append(news)

    db.add_all(news_list)
    db.commit()
    db.close()
