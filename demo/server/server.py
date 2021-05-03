import aiohttp
from aiohttp import web


# Функция для обработчика на сокетах
async def websocket_handler(request):
    socket = web.WebSocketResponse()
    idx = 0
    await socket.prepare(request)
    # Ожидание сообщения от клиента
    async for message in socket:
        if message.type == aiohttp.WSMsgType.TEXT:
            # Если сообщение пустое, не добавляем
            if message.data:
                # Добавление сообщения в БД
                idx += 1
                await socket.send_json({'id': idx, 'text': message.data})
    return socket
