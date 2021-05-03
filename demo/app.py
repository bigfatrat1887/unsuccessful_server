from aiohttp import web
import jinja2
import aiohttp_jinja2
from .routes import setup_routes


# Создание асинхронного приложения
async def create_app():
    app = web.Application()
    aiohttp_jinja2.setup(
        app,
        # Откуда берем HTML файлы для внешнего
        loader=jinja2.PackageLoader('demo', 'templates')
    )
    # Добавляем пути к сайтам
    setup_routes(app)
    return app

