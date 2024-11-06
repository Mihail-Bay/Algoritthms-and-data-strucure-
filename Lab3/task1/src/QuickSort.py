import random
import time
import tracemalloc
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Lab3.utils import read_input, write_output

# Начинаем отслеживание использования памяти
tracemalloc.start()

t_start = time.perf_counter()  # Запоминаем начало времени выполнения

def partition(l, low, high):
    # Выбираем случайный индекс для использования в качестве опорного элемента
    pivot_index = random.randint(low, high)
    # Меняем местами опорный элемент с элементом на позиции high
    l[pivot_index], l[high] = l[high], l[pivot_index]
    pivot = l[high]  # Устанавливаем опорный элемент
    i = low - 1  # Индекс для меньших элементов

    # Перебираем элементы от low до high - 1 (не включая опорный элемент)
    for j in range(low, high):
        # Если текущий элемент меньше или равен опорному
        if l[j] <= pivot:
            i += 1  # Увеличиваем индекс меньших
            # Меняем местами текущий элемент и элемент на позиции i
            l[i], l[j] = l[j], l[i]

    # После завершения цикла помещаем опорный элемент на его правильное место
    l[i + 1], l[high] = l[high], l[i + 1]
    return i + 1  # Возвращаем индекс, на котором находится опорный элемент


def randomized_quick_sort(l, low, high):
    # Проверяем, есть ли элементы для сортировки
    if low < high:
        # Получаем индекс опорного элемента, используя partition
        q = partition(l, low, high)
        # Рекурсивно сортируем подмассивы до и после опорного элемента
        randomized_quick_sort(l, low, q - 1)
        randomized_quick_sort(l, q + 1, high)


if __name__ == '__main__':
    n, l = read_input(task=1)

    n = int(n.strip())
    l = list(map(int, l.strip().split()))

    randomized_quick_sort(l, 0, n - 1)

    sl = (' '.join(map(str, l)))

    write_output(1, sl)

    # Вычисляем время выполнения
    elapsed_time = time.perf_counter() - t_start
    print(f"Время выполнения: {elapsed_time:.6f} секунд")

    # Получаем текущее использование памяти
    current, peak = tracemalloc.get_traced_memory()
    print(f"Текущая память: {current / 10 ** 6:.6f} МБ; Пиковая память: {peak / 10 ** 6:.6f} МБ")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()