CREATE TABLE IF NOT EXISTS mainmenu(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
url TEXT NOT NULL);

CREATE TABLE IF NOT EXISTS courses(
id INTEGER PRIMARY KEY AUTOINCREMENT,
title TEXT NOT NULL,
text TEXT NOT NULL,
price INTEGER NOT NULL,
url TEXT NOT NULL
);