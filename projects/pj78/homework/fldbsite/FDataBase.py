import sqlite3
import time
import math
import re
from flask import url_for


class FDataBase:
    def __init__(self, db):
        self.__db = db
        self.__cur = db.cursor()

    def get_menu(self):
        sql = "SELECT * FROM mainmenu"
        try:
            self.__cur.execute(sql)
            res = self.__cur.fetchall()
            if res:
                return res
        except IOError:
            print("Ошибка чтения из БД")
        return []

    def add_course(self, title, text, price, url):
        try:
            self.__cur.execute("SELECT COUNT() as `count` FROM courses WHERE url LIKE ?", (url,))
            res = self.__cur.fetchone()
            if res['count'] > 0:
                print("Курс с таким url уже существует")
                return False
            base = url_for('static', filename="images")
            text = re.sub(r"(?P<tag><img\s+[^>]*src=)(?P<quote>[\"'])(?P<url>.+?)(?P=quote)>", r"\g<tag>" + base + r"/\g<url>>", text)
            self.__cur.execute("INSERT INTO courses VALUES(NULL, ?, ?, ?, ?)", (title, text, price, url))
            self.__db.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления курса в БД" + str(e))
            return False
        return True

    def get_course(self, alias):
        try:
            self.__cur.execute(f"SELECT title, text FROM courses WHERE url = '{alias}'")
            res = self.__cur.fetchone()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения курса из БД" + str(e))
        return False, False

    def get_courses_annonce(self):
        try:
            self.__cur.execute(f'SELECT id, title, price, url, text FROM courses ORDER BY id')
            res = self.__cur.fetchall()
            if res:
                return res
        except sqlite3.Error as e:
            print("Ошибка получения курса из БД" + str(e))
            return False
        return []
