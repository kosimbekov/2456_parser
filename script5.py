# input ()
a = int(input("Введите свое число: "))
b = int(input("Введите свое число: "))
c = int(input("Введите свое число: "))
print(a + b + c)
total = a + b + c
if total % 2 == 0:
    print("Сумма четная")
else:
    print("Нечетная сумма")
