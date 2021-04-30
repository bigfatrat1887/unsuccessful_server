from aiohttp_jinja2 import template
from demo.db import db
# Добавляем обработчики (Совсем ничего не напоминает?)
# Шутка, это просто отправка HTML файлов через функции


@template('index.html')
async def index(request):
    response = db.execute_read_query("SELECT * from message")
    return {'data': response}


async def update(request):
    response = db.execute_read_query("SELECT * from message")
    return response


