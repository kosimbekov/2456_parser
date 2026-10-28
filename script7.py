# input ()
mounth = input("Введите месяц: ")
if mounth == "Декабрь" or mounth == "Январь" or mounth == "Февраль":
    print("Зима")
elif mounth == "Март" or mounth == "Апрель" or mounth == "Май":
    print("Весна")
elif mounth == "Июнь" or mounth == "Июль" or mounth == "Август":
    print("Лето")
elif mounth == "Сентябрь" or mounth == "Октябрь" or mounth == "Ноябрь":
    print("Осень")
else:
    print("Такого месяца не существует")