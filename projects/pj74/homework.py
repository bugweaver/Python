import sqlite3


phones_tpl = [
    ('Xiaomi Redmi Note 10 Pro', 13990),
    ('Samsung Galaxy A52',  24990),
    ('Honor 50 Lite', 22990),
    ('Realme 8', 12990),
    ('POCO M3 Pro', 14990),
]

with sqlite3.connect("smartphones.db") as con:
    cur = con.cursor()
    cur.execute("""
    CREATE TABLE IF NOT EXISTS phones(
        phone_id INTEGER PRIMARY KEY AUTOINCREMENT,
        model TEXT,
        price INTEGER
    )
    """)
    for phone in phones_tpl:
        cur.execute("INSERT INTO phones VALUES(NULL, ?, ?)", phone)
