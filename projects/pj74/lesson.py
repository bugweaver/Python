# import sqlite3

# cars_tpl = [
#     ('BMW', 54000),
#     ('Chevrolet', 46000),
#     ('Daewoo', 38000),
#     ('Citroen', 29000),
#     ('Honda', 33000),
# ]
# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#     cur.execute("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     )
#     """)
#
#     cur.executescript("""
#     DELETE FROM cars WHERE model LIKE 'B%';
#     UPDATE cars SET price = price + 100;
#     """)

# cur.execute("UPDATE cars SET price = :Price WHERE model LIKE 'B%'", {"Price": 0})

# cur.executemany("INSERT INTO cars VALUES(NULL, ?, ?)", cars_tpl)

# for car in cars_tpl:
#     cur.execute("INSERT INTO cars VALUES(NULL, ?, ?)", car)

# cur.execute("INSERT INTO cars VALUES(1, 'Renault', 22000)")
# cur.execute("INSERT INTO cars VALUES(2, 'Volvo', 29000)")
# cur.execute("INSERT INTO cars VALUES(3, 'Mercedes', 57000)")
# cur.execute("INSERT INTO cars VALUES(4, 'Bentley', 35000)")
# cur.execute("INSERT INTO cars VALUES(5, 'Audi', 52000)")

# con.commit() - сохраняет все изменения в БД
# con.close() - закрывает соединение с БД

# import sqlite3
# con = None
# try:
#
#     con = sqlite3.connect("car.db")
#
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#     );
#     BEGIN;
#     "INSERT INTO cars VALUES(NULL, 'Renault', 22000)";
#     UPDATE cars SET price = price + 100;
#     """)
#     con.commit()
#
# except sqlite3.Error as e:
#     if con:
#         con.rollback()
#     print("Ошибка выполнения запроса")
#
# finally:
#     if con:
#         con.close()

# import sqlite3
#
# with sqlite3.connect("car.db") as con:
#     cur = con.cursor()
#     cur.executescript("""
#     CREATE TABLE IF NOT EXISTS cars(
#         car_id INTEGER PRIMARY KEY AUTOINCREMENT,
#         model TEXT,
#         price INTEGER
#      );
#      CREATE TABLE IF NOT EXISTS cost(
#         name TEXT, tr_in INTEGER, buy INTEGER
#      )
#     """)

# cur.execute("INSERT INTO cars VALUES(NULL, 'Запорожец', 1000)")
# last_row_id = cur.lastrowid  # id последней записи
# buy_car_id = 2
# cur.execute("INSERT INTO cost VALUES('Илья', ?, ?)", (last_row_id, buy_car_id))

# cur.execute("SELECT model, price FROM cars")
#
# rows = cur.fetchall()
# print(rows)


# import sqlite3
#
#
# def read_ava(n):
#     try:
#         with open(f"avatars/{n}.png", "rb") as f:
#             return f.read()
#     except IOError as e:
#         print(e)
#         return False
#
#
# def write_ava(name, data):
#     try:
#         with open(name, "wb") as f:
#             f.write(data)
#     except IOError as e:
#         print(e)
#         return False
#     return True
#
#
# with sqlite3.connect("car.db") as con:
#     con.row_factory = sqlite3.Row
#     cur = con.cursor()
#     cur.executescript("""
#
#      CREATE TABLE IF NOT EXISTS users(
#         name TEXT, ava BLOB, score INTEGER
#      )
#     """)
#
#     cur.execute("Select ava FROM users")
#     img = cur.fetchone()['ava']
#
#     write_ava('out.png', img)
# img = read_ava(1)
# if img:
#     binary = sqlite3.Binary(img)
#     cur.execute("INSERT INTO users VALUES ('Илья', ?, 1000)", (binary,))


import sqlite3

with sqlite3.connect("car.db") as con:
    cur = con.cursor()
    with open("sql_dump", "w") as f:
        for sql in con.iterdump():
            f.write(sql)
