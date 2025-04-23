from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime
from .database import Base

class News(Base):
    __tablename__ = "news"

    id = Column(Integer, primary_key=True, index=True)
    source_name = Column(String(100), nullable=True)
    author = Column(String(255), nullable=True)
    title = Column(String(255))
    description = Column(Text, nullable=True)
    url = Column(String(255))
    url_to_image = Column(String(255), nullable=True)
    content = Column(Text, nullable=True)
    published_at = Column(DateTime, default=datetime.utcnow)
