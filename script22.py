str_1 = "123456789"
list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

str_1_len = 0
for _ in str_1:
    str_1_len += 1
print(str_1_len)



def print_hello():
    print("hello")
print_hello()



def show_user_info(name, age=18, phone="+998"):
    print(f"Hello user: {name}, Age: {age}, Phone: {phone}")


show_user_info("Ivan")
show_user_info("Bob", 27)
show_user_info("Bob", 27, "+998909300990" )
show_user_info(age=27, phone="+998909300990", name="Ivan")




def calculate_birth_year(age: int) -> int:
    return 2026 - age

print(calculate_birth_year(25))



def calculate(num_1, num_2, operator):
    if operator == "+":
        return num_1 + num_2
    elif operator == "-":
        return num_1 - num_2
    elif operator == "*":
        return num_1 * num_2
    elif operator == "/":
        if not num_2:
            return 0
        return num_1 / num_2
    else:
        return "Неизвестный оператор"
print(calculate(10,5,"+"))
print(calculate(10,5,"-"))
print(calculate(10,5,"*"))
print(calculate(10,5,"/"))


def make_pizza(testo, meat, cheese, *args, **kwargs):
    print(testo, meat, cheese)

make_pizza("слоенное", "говядина", "плавленный")
make_pizza("слоенное", "говядина", "плавленный", "перец", "чеснок", "сузьма")
make_pizza("слоенное", "говядина", "плавленный", "перец", "чеснок", "сузьма",
           payme=True, delivery=123)





