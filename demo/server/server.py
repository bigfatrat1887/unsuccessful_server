import aiohttp
from aiohttp import web
from demo.db import db


# Функция для обработчика на сокетах
async def websocket_handler(request):
    socket = web.WebSocketResponse()
    await socket.prepare(request)
    # Ожидание сообщения от клиента
    async for message in socket:
        if message.type == aiohttp.WSMsgType.TEXT:
            # Если сообщение пустое, не добавляем
            if message.data:
                # Добавление сообщения в БД
                await socket.send_str(message.data + '/added')
                db.execute_query(f"""
                INSERT INTO
                    message (message)
                VALUES
                    ('{message.data}');""")
    return socket
