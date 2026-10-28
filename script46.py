import json
import sqlite3
import urllib.request

DB_NAME = 'new_database.db'


def init_db():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY,
                first_name TEXT,
                last_name TEXT,
                email TEXT,
                username TEXT
            )
        ''')
        conn.commit()


def fetch_and_save_users():
    url = 'https://dummyjson.com'
    try:
        with urllib.request.urlopen(url) as response:
            data = json.loads(response.read().decode())
            users = data.get('users', [])

            with sqlite3.connect(DB_NAME) as conn:
                cursor = conn.cursor()
                for u in users:
                    cursor.execute('''
                        INSERT OR REPLACE INTO users (id, first_name, last_name, email, username)
                        VALUES (?, ?, ?, ?, ?)
                    ''', (
                        u['id'],
                        u['firstName'],
                        u['lastName'],
                        u['email'],
                        u['username']
                    ))
                conn.commit()
    except Exception:
        pass


def show_all_users():
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('SELECT id, first_name, last_name FROM users')
        for row in cursor.fetchall():
            print(f"ID: {row[0]} | Имя: {row[1]} {row[2]}")


def find_user_by_name(name):
    with sqlite3.connect(DB_NAME) as conn:
        cursor = conn.cursor()
        cursor.execute('''
            SELECT id, first_name, last_name, email, username
            FROM users
            WHERE first_name LIKE ? OR last_name LIKE ?
        ''', (f"%{name}%", f"%{name}%"))
        for row in cursor.fetchall():
            print(f"ID: {row[0]}")
            print(f"ФИО: {row[1]} {row[2]}")
            print(f"Email: {row[3]}")
            print(f"Username: {row[4]}")


def main():
    init_db()
    fetch_and_save_users()

    while True:
        command_input = input().strip()
        if not command_input:
            continue

        parts = command_input.split(maxsplit=1)
        cmd = parts[0].lower()

        if cmd == 'stop':
            break
        elif cmd == 'list':
            show_all_users()
        elif cmd == 'name' and len(parts) == 2:
            find_user_by_name(parts[1])


if __name__ == '__main__':
    main()

