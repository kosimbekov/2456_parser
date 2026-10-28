text = ('123')
num = 123

print(type(text))

def test():
    ...


print(type(test))
print(type(test()))

str()

class Human:
    living_planet = 'earth'

    arms = 2
    legs = 2

    def __init__(self, name):
        print('working', name)
        self.name = name

    def welcome(self):
        print(f"Hello from {self.name}")

    def __str__(self):
        return f"строковое значение: {self.name}"
human_1 = Human('human-1')
print(human_1.living_planet)
human_1.legs = 3

print(human_1.legs)

human_2 = Human('human-2')
human_2.welcome()
print(human_2)

class Worker:
    def __init__(self, name, age, salary, working_days):
        self.name = name
        self.age = age
        self.salary = salary
        self.working_days = working_days
    def get_daily_salary(self):
        return self.salary / self.working_days

    def __gt__(self, other):
        return self.salary > other.salary
    def __lt__(self, other):
        return self.salary < other.salary
    def __ge__(self, other):
        return self.salary >= other.salary
    def __eq__(self, other):
        return self.salary == other.salary
    def __ne__(self, other):
        return self.salary != other.salary
worker1 = Worker(name='worker-1', age=20, salary=100, working_days=10)
worker2 = Worker(name='worker-2', age=25, salary=45, working_days=10)
print(worker1)
print(worker2)
print(f"worker1: Зарплата за день: {worker1.get_daily_salary()}")
print(f"worker2: Зарплата за день: {worker2.get_daily_salary()}")
print(worker1.salary > worker2.salary)

