# print(name)
# print(1/0)
# print(int('abc'))
from typing import re

# def a()
#     pass


# while True:
#     num = input("num: ")
#
#     try:
#         num = int(num)
#         if num == 1:
#             print(username)
#         elif num == 2:
#             print(1/0)
#         elif num == 3:
#             print([][0])
#     except ValueError:
#         print("Не число")
#     except ZeroDivisionError:
#         print("нельзя делить на ноль")
#     except NameError:
#         print("переменная не найдена")
#     except IndexError:
#         print("неверный индекс")
#     except Exception as e:
#         print("ошибка", e, e.__class__)
#     else:
#         print("В блоке try нет ошибок:", num + 10)
#     finally:
#         print("запускаюсь всегда")


with open("mbox-short.txt") as file:
    content = file.read()

    pattern = r'\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}'
    result = re.findall(pattern, content)
    print(result)
