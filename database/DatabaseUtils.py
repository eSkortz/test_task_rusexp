from database.ConfigReader import database_config
import psycopg2
from psycopg2 import sql
from psycopg2.extensions import connection


def create_connection() -> connection:
    """создание соединение с базой данных

    Returns:
        connection: на выходе получаем объект типа <connection object>
    """
    connection = psycopg2.connect(
        database = database_config.DATABASE.get_secret_value(),
        user = database_config.USER.get_secret_value(),
        password = database_config.PASSWORD.get_secret_value(),
        host = database_config.HOST.get_secret_value(),
        port = database_config.PORT.get_secret_value()
    )
    return connection


def upsert_new_product(new_product: dict) -> None:
    """создание новой записи в мейнфрейме
    (используем insert on conflict для отработки случаев,
    когда такой продукт уже находится в мейнфрейме)

    Args:
        new_product (dict): словарь с данными по продукту
    """    
    connection = create_connection()
    cursor = connection.cursor()
    
    query = sql.SQL("""
        INSERT INTO mainframe (sid, category, name, price, cost_price, 
                                logistics, delivery, markup, sale_price, calculate)
        VALUES (%(sid)s, %(category)s, %(name)s, %(price)s, %(cost_price)s, %(logistics)s, 
                    %(delivery)s, %(markup)s, %(sale_price)s, %(calculate)s)
        ON CONFLICT (sid) DO UPDATE
        SET
            category = EXCLUDED.category,
            name = EXCLUDED.name,
            price = EXCLUDED.price,
            cost_price = EXCLUDED.cost_price,
            logistics = EXCLUDED.logistics,
            delivery = EXCLUDED.delivery,
            markup = EXCLUDED.markup,
            sale_price = EXCLUDED.sale_price,
            calculate = EXCLUDED.calculate
    """)
    cursor.execute(query, new_product)
    
    connection.commit()
    cursor.close()
    connection.close()
    

def get_percent_logistics() -> float:
    """функция для получения активного процента логистики
    (берется первая запись, в которой поле active=True)
    
    Returns:
        float: возвращаем сам процент
    """    
    connection = create_connection()
    cursor = connection.cursor()
    
    percent_query = """SELECT percent FROM logistics WHERE active = True"""
    cursor.execute(percent_query)
    percent = cursor.fetchone()[0]
    
    connection.commit()
    cursor.close()
    connection.close()
    
    return percent


def get_min_max_logistics() -> tuple:
    """функция для получения минимального и максимального значения
    логистики
    (берется первая запись, в которой поле active=True)

    Returns:
        tuple: возвращаем минимум и максимум
    """    
    connection = create_connection()
    cursor = connection.cursor()
    
    min_query = """SELECT min FROM logistics WHERE active = True"""
    cursor.execute(min_query)
    min_logistics = cursor.fetchone()[0]
    
    max_query = """SELECT max FROM logistics WHERE active = True"""
    cursor.execute(max_query)
    max_logistics = cursor.fetchone()[0]
    
    connection.commit()
    cursor.close()
    connection.close()
    
    return min_logistics, max_logistics


def get_percent_delivery() -> float:
    """функция для получения активного процента доставки
    (берется первая запись, в которой поле active=True)
    
    Returns:
        float: возвращаем сам процент
    """
    connection = create_connection()
    cursor = connection.cursor()
    
    percent_query = """SELECT percent FROM delivery WHERE active = True"""
    cursor.execute(percent_query)
    percent = cursor.fetchone()[0]
    
    connection.commit()
    cursor.close()
    connection.close()
    
    return percent


def get_min_max_delivery() -> tuple:
    """функция для получения минимального и максимального значения
    доставки
    (берется первая запись, в которой поле active=True)

    Returns:
        tuple: возвращаем минимум и максимум
    """   
    connection = create_connection()
    cursor = connection.cursor()
    
    min_query = """SELECT min FROM delivery WHERE active = True"""
    cursor.execute(min_query)
    min_delivery = cursor.fetchone()[0]
    
    max_query = """SELECT max FROM delivery WHERE active = True"""
    cursor.execute(max_query)
    max_delivery = cursor.fetchone()[0]
    
    connection.commit()
    cursor.close()
    connection.close()
    
    return min_delivery, max_delivery


def get_markup(category: int, cost_price: int) -> int:
    """функция для получения наценки по категории из таблицы cmm

    Args:
        category (int): передаем id категории
        cost_price (int): передаем себестоимость продукта

    Returns:
        int: получаем наценку по категории
    """
    
    # * Сверяем себестоимость для определения нужного столбца    
    if cost_price < 200:
        column = f'cp_{cost_price - (cost_price % 20)}'
    elif cost_price < 500:
        column = f'cp_{cost_price - (cost_price % 50)}'
    elif cost_price < 1000:
        column = f'cp_{cost_price - (cost_price % 100)}'
    elif cost_price < 3000:
        column = f'cp_{cost_price - (cost_price % 200)}'
    elif cost_price < 5000:
        column = 'cp_3000'
    elif cost_price < 10000:
        column = 'cp_5000'
    else:
        column = 'cp_10000'
        
    connection = create_connection()
    cursor = connection.cursor()
    
    cp_query = f"""SELECT {column} FROM cmm WHERE category_id = {category}"""
    cursor.execute(cp_query)
    # * в случае, если такая категори не была найдена, - обрабатывается исключение и
    # * берется процент по категории 'Not Found'
    try:
        cp = cursor.fetchone()[0]
    except TypeError:
        cp_notfound_query = f"""SELECT {column} FROM cmm WHERE category_id = 61401"""
        cursor.execute(cp_notfound_query)
        cp = cursor.fetchone()[0]
    return cp
    