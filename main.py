import uvicorn
from fastapi import FastAPI, HTTPException
from util import get_news, get_comments_for_one_news, get_comments_count_map

app = FastAPI(title="News")


@app.get("/news")
async def get_all_news():
    news = get_news()
    result = {'news': []}
    comments_count_map = get_comments_count_map()
    for n in news:
        n['comments_count'] = comments_count_map.get(n['id'], 0)
        result['news'].append(n)
    result['news_count'] = len(news)
    return result


@app.get("/news/{news_id}")
async def get_news_by_id(news_id: int):
    news = get_news()
    result = {}
    for n in news:
        if n['id'] == news_id:
            result = n
            break
    if not result:
        return HTTPException(status_code=404, detail='Такой новости не существует')
    result['comments'] = get_comments_for_one_news(news_id)
    result['comments_count'] = len(result['comments'])
    return result


if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
