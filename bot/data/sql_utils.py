import sqlite3
from sqlite3 import Error
from bot.config import path_db as db

def show_categories():
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        query = """
        SELECT * 
        FROM 'categories'
        """
        cursor.execute(query)
        categories = cursor.fetchall()
    except Error:
        print(Error)
    finally:
        conn.close()

    return categories

def print_products(product_id):
    try:
        conn = sqlite3.connection(db)
        cursor = conn.cursor()
        query = """
        SELECT * 
        FROM 'products'
        WHERE 'Id' =:Id
        """
        cursor.execute(query, {'Id': product_id})
        products = cursor.fetchall()
    except Error:
        print(Error)
    finally:
        conn.close()

    return products


