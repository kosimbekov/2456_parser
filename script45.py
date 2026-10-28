from database import functions  as db_funcs
from countryinfo import CountryInfo


def main():
    db_funcs.create_tables('countries.db')

    username = input('username: ')
    db_user = db_funcs.get_user_by_username('countries.db', username)
    if not db_user:
        db_user = db_funcs.insert_user('countries.db', username)

    while True:
        country = input('country: ')
        info = CountryInfo(country).info()
        print(info)


main()
