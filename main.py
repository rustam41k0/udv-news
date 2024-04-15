import uvicorn
from fastapi import FastAPI, HTTPException
from schemas import News, NewsDetail
from util import get_news, get_comments_for_one_news, get_comments_count_map, get_news_map

app = FastAPI(title="News")


@app.get("/news", response_model=News)
def get_all_news():
    news = get_news()
    result = {'news': []}
    comments_count_map = get_comments_count_map()
    for one_news_item in news:
        one_news_item['comments_count'] = comments_count_map.get(one_news_item['id'], 0)
        result['news'].append(one_news_item)
    result['news_count'] = len(news)
    return result


@app.get("/news/{news_id}", response_model=NewsDetail)
def get_news_by_id(news_id: int):
    news_map = get_news_map()
    if news_id not in news_map:
        raise HTTPException(status_code=404, detail='Такой новости не существует')
    result = news_map[news_id]
    result['comments'] = get_comments_for_one_news(news_id)
    result['comments_count'] = len(result['comments'])
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
