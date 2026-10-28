n = int(input("Введите первое число: "))
m = int(input("Введите второе число: "))
d = min(n, m)
while n % d != 0 or m % d != 0:
    d-=1
print(f"Наибольший общий делитель: {d}")














