from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class NewsOut(BaseModel):
    source_name: Optional[str]
    author: Optional[str]
    title: str
    description: Optional[str]
    url: str
    url_to_image: Optional[str]
    content: Optional[str]
    published_at: datetime

    class Config:
        from_attributes = True
