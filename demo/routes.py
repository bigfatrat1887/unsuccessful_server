from .views import frontend
from .server import websocket_handler
from aiohttp import web


# Cоздание путей для обработчиков
def setup_routes(app):
    app.router.add_routes(
        # Главная страница
        [web.get('/', frontend.index),
         # Websocket
         web.get('/ws', websocket_handler),
         # Обработчик скрипта дин.обновления
         web.post('/update', frontend.update)])
