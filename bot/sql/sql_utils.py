import sqlite3
from datatime import datetime
from dateutil import tz

def show_menu():
    conn = sqlite3.connect('bot.db')
    cursor = conn.cursor()
    query = """SELECT * FROM "Categories" WHERE "ParentCategory" = '0' """
    cursor.execute(query)
    Categories = cursor.fetchall()

    return Categories