from aiohttp import web
import jinja2
import aiohttp_jinja2
from .routes import setup_routes
from demo.db import db


# Создание асинхронного приложения
async def create_app():
    app = web.Application()
    # Первая инициализация БД
    # Если существует такая таблица, то ничего не выполняет
    db.execute_query("""
    CREATE TABLE IF NOT EXISTS message (
      id INTEGER PRIMARY KEY AUTOINCREMENT,
      message TEXT NOT NULL);""")
    aiohttp_jinja2.setup(
        app,
        # Откуда берем HTML файлы для внешнего
        loader=jinja2.PackageLoader('demo', 'templates')
    )
    # Добавляем пути к сайтам
    setup_routes(app)
    return app

