from aiohttp_jinja2 import template


# Добавляем обработчики (Совсем ничего не напоминает?)
# Шутка, это просто отправка HTML файлов через функции
@template('index.html')
async def index(request):
    return {}
