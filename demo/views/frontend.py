from aiohttp_jinja2 import template


# Главный обработчк с отображаемой страницей
@template('index.html')
async def index(request):
    return {}


