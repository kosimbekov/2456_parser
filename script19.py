dict_1 = {}
dict_2 = dict()

print(dict_1, dict_2)


contacts = {
    "bob": "+998909099090",
    "sam": 123456789,
    "tom": [123,123],
    "john": {
        "email": "john@gmail.com",
        "phone": 123
    }
}


# print(contacts)
# print(contacts["bob"])
# print(contacts.get("john"))
# contacts["sam"] = "hello"
# print(contacts)
#
# # deleted = contacts.pop("sam")
# # print(deleted)
# print(contacts.popitem())
# print(contacts)
# print(contacts.keys())
# print(contacts.values())
# print(contacts.items())
#
# for key in contacts.keys():
#     print(f"{key=}")
#
# for value in contacts.values():
#     print(value)

# for key, value in contacts.items():
#     print(key, value)



contacts_copy = contacts.copy()
print("Оригинал:", contacts)
print("Копия:", contacts_copy)

print(contacts["john"]["phone"])
print(contacts.get("john").get("email"))

products = [
    {"name": "product-1", "price": 10, "quantity": 5},
    {"name": "product-2", "price": 15, "quantity": 7},
    {"name": "product-3", "price": 20, "quantity": 10},


