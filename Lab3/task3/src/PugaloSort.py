import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Lab3.utils import read_input, write_output


def can_sort_matriochkas(n, k, sizes):
    # Создаем k списков для каждого сегмента
    segments = [[] for _ in range(k)]

    # Разбиваем массив на подмножества
    for i in range(n):
        segments[i % k].append(sizes[i])

    # Сортируем каждое подмножество
    for i in range(k):
        segments[i].sort()

    # Сборка отсортированного массива
    sorted_sizes = []
    for i in range(n):
        sorted_sizes.append(segments[i % k][i // k])

    # Проверяем, совпадает ли с отсортированным массивом
    if sorted_sizes == sorted(sizes):
        return "YES"
    else:
        return "NO"


if __name__ == "__main__":

    n, sizes = read_input(task=3)

    n, k = map(int, n.strip().split())
    sizes = list(map(int, sizes.strip().split()))

    result = can_sort_matriochkas(n, k, sizes)

    write_output(3, str(result))