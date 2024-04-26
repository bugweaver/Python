import sqlite3

with sqlite3.connect("users.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS person(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    phone BLOB NOT NULL DEFAULT NULL "+7909900000",
    age INTEGER CHECK(age > 0 AND age < 100)
    email TEXT UNIQUE
    )
    """)