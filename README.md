Выполнено в качестве тестового задания для UDV

Задача: необходимо разработать back-end сервиса новостей, в котором будет REST API  для получения новостей с комментариями.  

Требования:
* необходимо возвращать количество комментариев к каждой новости (поле "comments_count")
* возвращать необходимо не удаленные записи (поле "deleted")
* необходимо вернуть количество комментариев к текущей новости (поле "comments_count")
* в случае, если новости с таким id нет, необходимо вернуть код ошибки - 404
* в случае, если запись удалена (поле "deleted"), необходимо вернуть код ошибки - 404

Язык реализации Python (3.9 или старше)
Можно использовать фреймворки (Asyncio, AioHTTP, FastAPI)

Даны файлы news.json, в котором находится список новостей, и comments.json, в котором находятся комментарии к новостям, сопоставление по полю "news_id".  

GET "/" - возвращает список новостей  
GET "/news/{id}" - возвращает новость по ее id