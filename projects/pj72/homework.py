import sqlite3
with sqlite3.connect("students.db") as con:
    cur = con.cursor()
    