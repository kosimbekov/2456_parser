import requests
import sqlite3

connection = sqlite3.connect('json.db')
cursor = connection.cursor()

cursor.executescript('''
CREATE TABLE IF NOT EXISTS users(
id INTEGER PRIMARY KEY AUTOINCREMENT,
name TEXT,
username TEXT,
email TEXT,
company TEXT
);
CREATE TABLE IF NOT EXISTS posts(
id INTEGER PRIMARY KEY,
userID INTEGER,
title TEXT,
body TEXT
);
CREATE TABLE IF NOT EXISTS comments(
id INTEGER PRIMARY KEY,
postID INTEGER,
name TEXT,
email TEXT,
body TEXT
);
CREATE TABLE IF NOT EXISTS albums(
id INTEGER PRIMARY KEY,
userID INTEGER,
title TEXT
);
CREATE TABLE IF NOT EXISTS photos(
id INTEGER PRIMARY KEY,
albumID INTEGER,
title TEXT,
url TEXT,
thumbnailUrl TEXT
);
CREATE TABLE IF NOT EXISTS todos(
id INTEGER PRIMARY KEY,
userID INTEGER,
title TEXT,
completed INTEGER
);
CREATE TABLE IF NOT EXISTS weather(
id INTEGER PRIMARY KEY AUTOINCREMENT,
city TEXT,
temperature REAL,
description TEXT,
requested_at TEXT DEFAULT CURRENT_TIMESTAMP
);
''')

def create_database():
    connection = sqlite3.connect('json.db')
    cursor = connection.cursor()

def get_data(table):
    response = requests.get(
        f'https://jsonplaceholder.typicode.com/{table}'
    )
    response.raise_for_status()
    return response.json()

def save_data(table, data):
    connection = sqlite3.connect('json.db')
    cursor = connection.cursor()

    for item in data:
        if table == 'users':
            cursor.execute(
            'INSERT OR REPLACE INTO users VALUES (?, ?, ?, ?, ?)',
            (
                item['id'],
                item['name'],
                item['username'],
                item['email'],
                item['company']['name']
            )
        )

        elif table == 'posts':
             cursor.execute(
            'INSERT OR REPLACE INTO posts VALUES (?, ?, ?, ?)',
            (
                item['id'],
                item['userId'],
                item['title'],
                item['body']
            )
        )

        elif table == 'comments':
             cursor.execute(
            'INSERT OR REPLACE INTO comments VALUES (?, ?, ?, ?, ?)',
            (
                item['id'],
                item['postId'],
                item['name'],
                item['email'],
                item['body']
            )
        )

        elif table == 'albums':
             cursor.execute(
            'INSERT OR REPLACE INTO albums VALUES (?, ?, ?)',
            (
                item['id'],
                item['userId'],
                item['title']
            )
        )

        elif table == 'photos':
             cursor.execute(
            'INSERT OR REPLACE INTO photos VALUES (?, ?, ?, ?, ?)',
            (
                item['id'],
                item['albumId'],
                item['title'],
                item['url'],
                item['thumbnailUrl']
            )
        )

        elif table == 'todos':
            cursor.execute(
            'INSERT OR REPLACE INTO todos VALUES (?, ?, ?, ?)',
            (
                item['id'],
                item['userId'],
                item['title'],
                int(item['completed'])
            )
        )

def main():
    create_database()

    tables = ['users', 'posts', 'comments', 'albums', 'photos', 'todos']
    for table in tables:
        try:
            data = get_data(table)
            save_data(table, data)
            print(f'{table} saved successfully')
        except requests.RequestException as error:
            print(f'Error loading {table}: {error}')

main()

connection.commit()
connection.close()