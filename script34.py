class Student:
    def __init__(self, name="Ivan", age=18, groupNumber="10A"):
        self.name = name
        self.age = age
        self.groupNumber = groupNumber
    def getName(self):
        return self.name
    def getAge(self):
        return self.age
    def getGroupNumber(self):
        return self.groupNumber
    def setNameAge(self, new_name, new_age):
        self.name = new_name
        self.age = new_age
    def setGroupNumber(self, new_group):
        self.groupNumber = new_group
s1 = Student("Боб", 19, "10B")
s2 = Student("Амир", 17, "11A")
s3 = Student("Олег", 18, "10V")
s4 = Student("Бехруз", 20, "11E")
s5 = Student()
s5.setNameAge("Сергей", 21)
s5.setGroupNumber("12A")
all_students = [s1, s2, s3, s4, s5]
for student in all_students:
    print(f"Имя: {student.getName()}, Возраст: {student.getAge()}, Группа: {student.getGroupNumber()}")

