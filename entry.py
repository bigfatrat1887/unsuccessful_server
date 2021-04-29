import aiohttp
import asyncio
import logging
import websockets
# Импорт приложения из внешнего файла
from demo import create_app


# Cоздаем проиложение
app = create_app()


async def server(websocket, path):
    async for message in websocket:
        await websocket.send(f'{message}')

if __name__ == '__main__':
    # Запустим приложение
    logging.basicConfig(level=logging.DEBUG)
    aiohttp.web.run_app(app, port=5000)
    start_server = websockets.serve(server, "localhost", 5000)
    asyncio.get_event_loop().run_until_complete(start_server)
    asyncio.get_event_loop().run_forever()







