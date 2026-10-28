import sqlite3
# pip install requests
# подключение к БД
connection = sqlite3.connect('json.db')

# создаем объект для выполнения запросов в БД
cursor = connection.cursor()

# выполняет 1 запрос за 1 раз
# написать SQL запрос на создание таблицы users
# id
# name
# username
# email
# company
cursor.execute('''
create table if not exists users(
    id integer primary key autoincrement,
    name text,
    username text,
    email text,
    company text
);
''')
# INSERT , UPDATE, DELETE, CREATE DROP ALTER
connection.commit()
# cursor.executescript()
# написать 3 INSERT для добавления данных в таблицу users
# insert into
# cursor.executescript('''
# insert into users(name, username, email, company) values ("test-1", "test-1", "test-1", "test-1");
# insert into users(name, username, email, company) values ("test-2", "test-2", "test-2", "test-2");
# insert into users(name, username, email, company) values ("test-3", "test-3", "test-3", "test-3");
# ''')
# cursor.execute('select * from users;')
# cursor.fetchall()
# cursor.fetchone()
# print(cursor.fetchone())

# sql injection
# cursor.execute('''
# insert into users(name, username, email, company)
# values (?, ?, ?, ?);
# ''', ['Bob', 'bobob', 'bob@gmail.com', 'bob company'])
#
# connection.commit()
# cursor.execute('select * from users;')
# print(cursor.fetchall())

# cursor.executemany()
# закрываем соединение с БД

users = [(f'User#{i}', f'UserUser#{i}', f'UserEmail#{i}@gmail.com', f'UserCompany#{i}') for i in range(5, 21)]
cursor.executemany('''
insert into users(name, username, email, company)
values (?, ?, ?, ?);
''', users)
cursor.execute('select * from users;')
print(cursor.fetchall())
connection.close()