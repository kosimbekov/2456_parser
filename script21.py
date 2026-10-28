schedule = {}
days_count = int(input("На сколько дней хотите ввести расписание?: "))
for i in range(days_count):
    day = input(f"Введите день недели №{i+1}: ").strip().capitalize()
    lessons_input = input(f"Введите занятие на {day} (через запятую): ")
    lessons_list = [lesson.strip() for lesson in lessons_input.split(",")]
    schedule[day] = lessons_list
print("--- Полное расписание на неделю ---")
for day, lessons in schedule.items():
    print(f"{day}: {', '.join(lessons)}")
print("--- Поиск расписания ---")
search_day = input("Введите день недели для проверки: ").strip().capitalize()
if search_day in schedule:
    print(f"Занятие на {search_day}: {', '.join(schedule[search_day])}")
else:
    print("На этот день расписания нет.")
