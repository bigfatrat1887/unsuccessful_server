from .views import frontend
from aiohttp import web


# Cоздание заглушки для сайта
def setup_routes(app):
    # Добавить возможность циклического считывания
    app.router.add_routes([web.get('/', frontend.index)])
