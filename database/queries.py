TABLE_EXISTS_SQL = """
select name from sqlite_master
where type='table' and name = ?;
"""
USERS_TABLE_SQL = """
create table if not exists users (
id integer primary key autoincrement,
username text not null,
user_name text not null unique
);
"""
COUNTRIES_TABLE_SQL = """
create table if not exists countries (
id integer primary key autoincrement,
name text not null,
population integer,
area integer,
region text,
capital text,
user_id integer reference users(id)
);
"""
USER_GET_SQL = """
select * from users
where id = ?;
"""
USER_INSERT_SQL = """
insert into users (username) values (?)
on conflict (username) do nothing
returning *;
"""
COUNTRY_INSERT_SQL = """
insert into countries (name, capital, region, area, population, user_id)
values (?, ?, ?, ?, ?, ?);
"""
COUNTRIES_BY_USER_SQL = """
select * from countries
where user_id = ?;
"""