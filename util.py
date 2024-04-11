import json


def get_news() -> list:
    with open('news.json', 'r') as file:
        raw_news = json.load(file)
    news_filtered = list(filter(lambda x: not x['deleted'], raw_news['news']))
    return news_filtered


def get_comments_for_one_news(news_id: int) -> list:
    with open('comments.json', 'r') as file:
        comments = json.load(file)
    return list(filter(lambda x: x['news_id'] == news_id, comments['comments']))


def get_comments_count_map() -> dict:
    with open('comments.json', 'r') as file:
        comments = json.load(file)
    comments_count_map = {}  # news_id: comments_count
    for comm in comments['comments']:
        comments_count_map[comm['news_id']] = comments_count_map.get(comm['news_id'], 0) + 1
    return comments_count_map
