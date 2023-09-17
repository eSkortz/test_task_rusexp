from ConfigReader import database_config
import psycopg2
from psycopg2.extensions import connection, cursor


def create_connection() -> connection:
    """создаем соединение с базой данных

    Returns:
        Any: на выходе получаем объект типа <connection object>
    """
    connection = psycopg2.connect(
        database = database_config.DATABASE.get_secret_value(),
        user = database_config.USER.get_secret_value(),
        password = database_config.PASSWORD.get_secret_value(),
        host = database_config.HOST.get_secret_value(),
        port = database_config.PORT.get_secret_value()
    )
    return connection


def upsert_new_product() -> None:
    connection = create_connection()
    cursor = connection.cursor()
    query = """"""
    cursor.execute(query)
    connection.commit()
    cursor.close()
    connection.close()
    

def get_percent_logistics() -> float:
    connection = create_connection()
    cursor = connection.cursor()
    percent_query = """"""
    percent = cursor.execute(percent_query)
    connection.commit()
    cursor.close()
    connection.close()
    return percent


def get_min_max_logistics() -> tuple:
    connection = create_connection()
    cursor = connection.cursor()
    min_query = """"""
    min_logistics = cursor.execute(min_query)
    max_query = """"""
    max_logistics = cursor.execute(max_query)
    connection.commit()
    cursor.close()
    connection.close()
    return (min_logistics, max_logistics)


def get_percent_delivery() -> float:
    connection = create_connection()
    cursor = connection.cursor()
    percent_query = """"""
    percent = cursor.execute(percent_query)
    connection.commit()
    cursor.close()
    connection.close()
    return percent


def get_min_max_delivery() -> tuple:
    connection = create_connection()
    cursor = connection.cursor()
    min_query = """"""
    min_delivery = cursor.execute(min_query)
    max_query = """"""
    max_delivery = cursor.execute(max_query)
    connection.commit()
    cursor.close()
    connection.close()
    return (min_delivery, max_delivery)


def get_markup(category: str, cost_price: int) -> float:
    pass