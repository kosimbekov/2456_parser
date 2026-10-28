class Animal:
    def __init__(self, name):
        self.name = name

    def move(self):
        print(f"{self.name} передвигаться")

    # def __str__(self):
    #     return f"name={self.name}, sound={self.sound}"
    #
    # def make_sound(self):
    #     return f"{self.name} издает звук: {self.sound}"


# cat = Animal('cat', 'meow')
# print(cat)



class Dog(Animal):
    def bark(self):
        print(f"{self.name}")


dog = Dog("sharik")
dog.move()
dog.bark()

class Puppy(Dog):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

puppy = Puppy('puppy', 1)



class Vehicle:
    def __init__(self, brand, speed):
        self.brand = brand
        self.speed = speed

class Car(Vehicle):
    def __init__(self, brand, speed, doors):
        super().__init__(brand, speed)
        self.doors = doors

car = Car('Toyota', 180, 4)
print(car.brand, car.speed, car.doors)


class Account:
    def __init__(self, owner, balance):
        self.owner = owner
        self._balance = balance
        self.__pin = '0000'

    def deposit(self, amount):
        if amount > 0:
            self._balance += amount

    @property
    def balance(self):
        return self._balance

acc = Account('Ildar', 1000)
acc.deposit(100)
print(acc.balance)



class Student:
    def __init__(self):
        self._grades = []
    def addGrade(self, grade):
        if 2 <= grade <= 5:
            self._grades.append(grade)
        else:
            print(f"Оценка {grade} вне диапозона 2-5 и не будет добавлена.")

student = Student()
student.addGrade(5)
student.addGrade(4)
student.addGrade(3)
student.addGrade(1)
student.addGrade(6)
print("Список оценок:", student._grades)



class Animal:
    def speak(self):
        return "Звук"


class Dog(Animal):
    def speak(self):
        return "Гав"


class Cat(Animal):
    def speak(self):
        return "мяу"

for animal in [Cat(), Dog(), Animal()]:
    print(animal.speak())


from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int

point = Point(1, 2)
print(point)





