import aiohttp
from aiohttp import web
from demo.db import db


async def websocket_handler(request):
    socket = web.WebSocketResponse()
    await socket.prepare(request)

    async for message in socket:
        if message.type == aiohttp.WSMsgType.TEXT:
            if message.data:
                await socket.send_str(message.data + '/added')
                db.execute_query(f"""
                INSERT INTO
                    message (message)
                VALUES
                    ('{message.data}');""")

    return socket
