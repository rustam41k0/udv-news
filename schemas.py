from datetime import datetime
from typing import List

from pydantic import BaseModel


class OneNewsItem(BaseModel):
    id: int
    title: str
    date: datetime
    body: str
    deleted: bool
    comments_count: int


class News(BaseModel):
    news: List[OneNewsItem]
    news_count: int


class Comment(BaseModel):
    id: int
    news_id: int
    title: str
    date: datetime
    comment: str


class NewsDetail(OneNewsItem):
    comments: List[Comment]
