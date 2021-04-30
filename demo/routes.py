from .views import frontend
from .server import websocket_handler
from aiohttp import web


# Cоздание заглушки для сайта
def setup_routes(app):
    # Добавить возможность циклического считывания
    app.router.add_routes([web.get('/', frontend.index),
                           web.get('/ws', websocket_handler),
                           web.post('/update', frontend.update)])
