import sqlite3
from . import queries


def connect_db(db_name):
    connection = sqlite3.connect(db_name)
    cursor = connection.cursor()
    return connection, cursor

def create_table(db_name, table_name, sql):
    connection, cursor = connect_db(db_name)
    cursor.execute(sql)
    connection.commit()
    print(f'table {table_name} created')

def is_table_exists(db_name, table_name):
    connection, cursor = connect_db(db_name)
    result = cursor.execute(queries.TABLE_EXISTS_SQL, [table_name]).fetchone()
    return result is not None


# написать функции для следующих запросов
# USER_GET_SQL get_user_by_username
# COUNTRIES_BY_USER_SQL  get_user_countries
def get_user_by_username(db_name, username):
    connection, cursor = connect_db(db_name)
    user = cursor.execute(queries.USER_GET_SQL, [username]).fetchone()
    return user

def get_user_countries(db_name, username):
    connection, cursor = connect_db(db_name)
    user = get_user_by_username(db_name, username)
    if not user:
        return []
    return cursor.execute(queries.COUNTRIES_BY_USER_SQL, [user[0]]).fetchall()


def create_tables(db_name):
    users_table_exists = is_table_exists(db_name, 'users')
    countries_table_exists = is_table_exists(db_name, 'countries')
    if not users_table_exists and not countries_table_exists:
        create_table(db_name, 'users', queries.USERS_TABLE_SQL)
        create_table(db_name, 'countries', queries.COUNTRIES_TABLE_SQL)
    else:
        print('tables already exist')


def insert_user(db_name, username):
    connection, cursor = connect_db(db_name)
    cursor.execute(queries.USER_INSERT_SQL, [username])
    user = cursor.fetchone()
    connection.commit()
    print(f'user {username} created')
    return user


def insert_country(db_name, *args):
    connection, cursor = connect_db(db_name)
    cursor.execute(queries.COUNTRIES_INSERT_SQL, args)
    connection.commit()
    print(f'country created')


