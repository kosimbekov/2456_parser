students = int(input("Введите количество студентов: "))
students_dict = {}
for i in range(students):
    name = input("Введите имя студента ")
    grade = float(input(f"Введите оценку для {name}: "))
    students_dict[name] = grade
grades = list(students_dict.values())
sum_grades = sum(grades)
max_grade = max(grades)
min_grade = min(grades)
print(f"Словарь;", students_dict)
print(f"Средняя оценка: {sum_grades:.2f}")
print(f"Максимальная оценка: {max_grade}")
print(f"Минимальная оценка: {min_grade}")

