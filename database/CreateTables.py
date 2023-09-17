from psycopg2.extensions import cursor
from DatabaseUtils import create_connection


def create_categories(cursor: cursor) -> None:
    """функция для создания таблицы categories

    Args:
        cursor (<cursor object>): даем функции на вход курсор
    """
    create_table_query = """
        CREATE TABLE IF NOT EXISTS categories 
        ( 
            id SERIAL PRIMARY KEY, 
            name VARCHAR(255) UNIQUE, 
            category_id INT UNIQUE 
        );"""
    cursor.execute(create_table_query)
    
    
def create_cmm(cursor: cursor) -> None:
    """функция для создания таблицы cmm

    Args:
        cursor (<cursor object>): даем функции на вход курсор
    """    
    create_table_query = """
        CREATE TABLE IF NOT EXISTS cmm 
        (
            id SERIAL PRIMARY KEY,
            category_id INT UNIQUE,
            cp_0 INT,
            cp_20 INT,
            cp_40 INT, 
            cp_60 INT,
            cp_80 INT,
            cp_100 INT,
            cp_120 INT,
            cp_140 INT,
            cp_160 INT,
            cp_180 INT,
            cp_200 INT,
            cp_250 INT,
            cp_300 INT,
            cp_350 INT,
            cp_400 INT,
            cp_450 INT,
            cp_500 INT,
            cp_600 INT,
            cp_700 INT, 
            cp_800 INT,
            cp_900 INT,
            cp_1000 INT,
            cp_1200 INT,
            cp_1400 INT,
            cp_1600 INT,
            cp_1800 INT,
            cp_2000 INT,
            cp_2200 INT, 
            cp_2400 INT,
            cp_2600 INT,
            cp_2800 INT,
            cp_3000 INT,
            cp_5000 INT,
            cp_10000 INT 
        );"""
    cursor.execute(create_table_query)
    
    
def create_logisctics(cursor: cursor) -> None:
    """функция для создания таблицы logistics

    Args:
        cursor (<cursor object>): даем функции на вход курсор
    """    
    create_table_query = """
        CREATE TABLE IF NOT EXISTS logistics
        (
            id SERIAL PRIMARY KEY,
            percent FLOAT,
            min INT,
            max INT,
            active BOOL
        );"""
    cursor.execute(create_table_query)
    
    
def create_delivery(cursor: cursor) -> None:
    """функция для создания таблицы delivery

    Args:
        cursor (<cursor object>): даем функции на вход курсор
    """    
    create_table_query = """
        CREATE TABLE IF NOT EXISTS delivery
        (
            id SERIAL PRIMARY KEY,
            percent FLOAT,
            min INT,
            max INT,
            active BOOL
        );"""
    cursor.execute(create_table_query)
    

def create_mainframe(cursor: cursor) -> None:
    """функция для создания таблицы mainframe

    Args:
        cursor (<cursor object>): даем функции на вход курсор
    """    
    create_table_query = """
        CREATE TABLE IF NOT EXISTS mainframe 
        (
            id SERIAL PRIMARY KEY,
            sid INT UNIQUE,
            category INT,
            name VARCHAR(255),
            price INT,
            cost_price FLOAT,
            logistics FLOAT,
            delivery FLOAT,
            markup INT,
            sale_price FLOAT,
            calculate INT
        );"""
    cursor.execute(create_table_query)


def create_indexes(cursor: cursor) -> None:
    """функция для создания индексов

    Args:
        cursor (<cursor object>): даем функции на вход курсор
    """    
    query = """ CREATE INDEX index_categories_name ON categories (name); """
    cursor.execute(query)
    query = """ CREATE INDEX index_categories_category_id ON categories (category_id); """
    cursor.execute(query)
    query = """ CREATE INDEX index_cmm_category_id ON cmm (category_id); """
    cursor.execute(query)
    query = """ CREATE INDEX index_mainframe_sid ON mainframe (sid); """
    cursor.execute(query)
    

def main() -> None:
    # * Создаем соединение с бд
    connection = create_connection()
    # * Создаем курсор
    cursor = connection.cursor()
    
    # * Создаем таблицы и индексы
    create_categories(cursor)
    create_cmm(cursor)
    create_logisctics(cursor)
    create_delivery(cursor)
    create_mainframe(cursor)
    create_indexes(cursor)
    
    # * комитим операции и закрываем курсор и соединение
    connection.commit()
    cursor.close()
    connection.close()
    

if __name__ == '__main__':
    main()