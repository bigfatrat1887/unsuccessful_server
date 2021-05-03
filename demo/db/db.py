import sqlite3
from sqlite3 import Error


def create_connection(path):
    # Попробуем подключиться к базе данных
    try:
        connection = sqlite3.connect(path)
        # Обработчик ошибки
    except Error as e:
        print(f"The error '{e}' occurred")
    return connection


# Создадим общий путь для базы данных, который поставим по стандарту
base = create_connection('demo/db/test.sqlite')


# Функция выполнения запроса SQL ( Кроме получения данных )
def execute_query(query, connection=base):
    # Инициализируем объект взаимодействия с БД
    cursor = connection.cursor()
    try:
        # Выполнить переданный запрос к БД
        cursor.execute(query)
        connection.commit()
        # Обработчик ошибки
    except Error as e:
        print(f"The error '{e}' occurred")


# Функция выполнения запроса по получению данных из SQL
def execute_read_query(query, connection=base):
    # Инициализируем объект взаимодействия с БД
    cursor = connection.cursor()
    try:
        # Выполнить переданный запрос к БД
        cursor.execute(query)
        # Возврат данных
        result = cursor.fetchall()
        return result
        # Обработчик ошибки
    except Error as e:
        print(f"The error '{e}' occurred")



