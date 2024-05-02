import sqlite3

with sqlite3.connect("db_4.db") as con:
    cur = con.cursor()
    cur.execute("""
    SELECT *
    FROM Ware
    ORDER BY Price DESC
    LIMIT 2, 5
    """)

    res = cur.fetchall()  # [(), ()]
    print(res)

    for res in cur:
        print(res)

    res2 = cur.fetchall()  # [(), ()]
    print(res2)

    res = cur.fetchone()
    print(res)

    res1 = cur.fetchmany(2)  # [(), ()]
    print(res1)
