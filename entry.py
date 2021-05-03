import aiohttp
import logging
# Импорт приложения из внешнего файла
from demo import create_app

# Cоздаем проиложение
app = create_app()
# Создадим сервер


if __name__ == '__main__':
    # Отобразим логи сервера
    logging.basicConfig(level=logging.DEBUG)
    aiohttp.web.run_app(app, port=5000)








