from aiohttp import web
from aiohttp_jinja2 import template
from demo.db import db
# Добавляем обработчики


# Главный обработчк с отображаемой страницей
@template('index.html')
async def index(request):
    # Возврат данных для Jinja
    return {'resp': db.execute_read_query("SELECT * from message")}


# Обработчик для динамического обновления страницы
async def update(request):
    # как бы то же самое, но другое
    return web.json_response({'resp': db.execute_read_query("SELECT * from message")})


