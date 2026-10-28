# from unittest import result
#
#
# def test_function(text):
#     return text + "1-2-3"
#
#
# print(test_function("hello"))
#
# function = test_function
#
# print(function("123"))
#
#
# def do_operation(n1, n2, operation):
#     result = operation(n1, n2)
# print(f"{result=}")
#
#
# def plus(num1, num2):
#     return num1 + num2
# do_operation(10, 5, plus)


words = ['hello', "programming", "food"]
words_2 = []

def make_upper(w):
    return f"{w} word'.upper()"


for item in words:
    words_2.append((item + ' ' + "word").upper())


print(words_2)

print(list(map(make_upper, words)))
print(list(map(list, words)))
print(list(map(str.upper, words)))

products = ["product-1", "product-2", "product-3"]
prices = [105, 110, 115]
result = []
for i in range(len(products)):
    result.append(f"{products[i]} {prices[i]}")
print(result)

def plus_2(i1, i2):
    return f"{i1} + {i2}"

print(list(map(plus_2, products, prices)))





