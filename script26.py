filename = "mbox-short.txt"
count = 0
file = open(filename, mode="r", encoding="utf-8")
for line in file:
    line = line.strip()
    if line.startswith("From "):
        words = line.split()
        email = words[1]
        print(email)
        count = count + 1
file.close()
print("Всего адресов:", count)
