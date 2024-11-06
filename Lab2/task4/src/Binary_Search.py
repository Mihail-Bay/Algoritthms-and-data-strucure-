import time
import tracemalloc  # Импортируем модуль для отслеживания памяти
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Lab2.utils import read_input, write_output

# Начинаем отслеживание использования памяти
tracemalloc.start()

t_start = time.perf_counter()  # Запоминаем начало времени выполнения


def binary_search(l, x):

    left, right = 0, len(l) - 1  # Устанавливаем пределы поиска

    while left <= right:  # Пока левый индекс меньше или равен правому
        mid = (left + right) // 2  # Находим середину
        if l[mid] == x:  # Если элемент в середине равен искомому
            return mid  # Возвращаем индекс
        elif l[mid] < x:  # Если элемент в середине меньше искомого
            left = mid + 1  # Ищем в правой части
        else:  # Если элемент в середине больше искомого
            right = mid - 1  # Ищем в левой части

    return -1  # Если элемент не найден, возвращаем -1


if __name__ == '__main__':
    '''# Чтение данных из файла input.txt
    with open('../txtf/input.txt', 'r') as f:
        n = int(f.readline().strip())  # Читаем число элементов в массиве
        l = list(map(int, f.readline().strip().split()))  # Читаем отсортированный массив
        k = int(f.readline().strip())  # Читаем число значений для поиска
        queries = list(map(int, f.readline().strip().split()))  # Читаем значения для поиска

    # Список для сохранения результатов
    r = []

    # Проходим по каждому элементу из queries
    for q in queries:
        ind = binary_search(l, q)  # Ищем индекс элемента в массиве
        r.append(ind)  # Добавляем результат в список

    # Запись результата в файл output.txt
    with open('../txtf/output.txt', 'w') as f:
        f.write(' '.join(map(str, r)))  # Записываем индексы, разделяя пробелами'''

    n, l, k, queries = read_input(task=4)
    n = int(n.strip())  # Читаем число элементов в массиве
    l = list(map(int, l.strip().split()))  # Читаем отсортированный массив
    k = int(k.strip())  # Читаем число значений для поиска
    queries = list(map(int,queries.strip().split()))  # Читаем значения для поиска

    r = []

    # Проходим по каждому элементу из queries
    for q in queries:
        ind = binary_search(l, q)  # Ищем индекс элемента в массиве
        r.append(ind)  # Добавляем результат в список

    r = (' '.join(map(str, r)))

    write_output(4, r)

    # Вычисляем время выполнения
    elapsed_time = time.perf_counter() - t_start
    print(f"Время выполнения: {elapsed_time:.6f} секунд")

    # Получаем текущее использование памяти
    current, peak = tracemalloc.get_traced_memory()
    print(f"Текущая память: {current / 10**6:.6f} МБ; Пиковая память: {peak / 10**6:.6f} МБ")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()