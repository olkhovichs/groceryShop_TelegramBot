import sqlite3
from sqlite3 import Error
from utils.config import path_db as db

'''def show_categories():
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

    return categories'''


def show_products():
    try:
        conn = sqlite3.connect(db)
        cursor = conn.cursor()
        query = """
        SELECT *
        FROM 'items'
        """
        cursor.execute(query)
        products = cursor.fetchall()
    except Error:
        print(Error)
    finally:
        conn.close()

    return products


'''def show_products(product_id):
    try:
        conn = sqlite3.connection(db)
        cursor = conn.cursor()
        query = """
        SELECT * 
        FROM 'products'
        """
        cursor.execute(query, {'Id': product_id})
        products = cursor.fetchall()
    except Error:
        print(Error)
    finally:
        conn.close()

    return products'''


