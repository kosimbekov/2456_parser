# input ()
# weather = input("Введите вашу погоду: ")
# if weather == "Жара" or weather == "Духота":
#     print("у вас жарко")
# elif weather == "Дождь" or weather == "Снег":
#     print("у вас холодно")
# else:
#     print("погода указана неправильно")



username = input("username: ")
password = input("password: ")

if username == username and not password:
    print("password empty")
elif not username and password:
    print("username empty")
elif not username and not password:
    print("username and password empty")
elif username == "Oleg" and password == "123":
    print(f"Admin: {username}")
elif username == "Igor" and password == "321":
    print(f"Member: {username}")
