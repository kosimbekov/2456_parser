import time
import sys
def timer_and_size_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        size_bytes = sys.getsizeof(result)
        print(f"Время выполнения: {execution_time:.6f} сек")
        print(f"Размер сформированного списка: {size_bytes} байт")
        return result
    return wrapper
@timer_and_size_decorator
def create_list(n):
    if n > 100000:
        return list(range(1, n + 1))
n = int(input("Введите n (не больше 100000): "))
my_list = create_list(n)

