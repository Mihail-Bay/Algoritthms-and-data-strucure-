import random

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Lab3.utils import read_input, write_output, decorate


def partition3(l, low, high):
    pivot_index = random.randint(low, high)
    l[pivot_index], l[high] = l[high], l[pivot_index]  # Ставим опорный элемент в конец
    pivot = l[high]  # Опорный элемент
    i = low  # Индекс для меньших элементов
    j = high - 1  # Индекс для больших элементов

    while i <= j:
        if l[i] < pivot:  # Если текущий элемент меньше опорного
            i += 1
        elif l[i] > pivot:  # Если текущий элемент больше опорного
            l[i], l[j] = l[j], l[i]  # Меняем местами
            j -= 1
        else:  # Если элемент равен опорному
            i += 1

    # Перемещаем все равные элементы к опорному элементу
    l[i], l[high] = l[high], l[i]
    return i, j  # Возвращаем границы равных элементов

def randomized_quick_sort(l, low, high):
    if low < high:
        m1, m2 = partition3(l, low, high)  # Используем трёхстороннее разбиение
        randomized_quick_sort(l, low, m1 - 1)  # Сортируем подмассив меньше опорного
        randomized_quick_sort(l, m2 + 1, high)  # Сортируем подмассив больше опорного


def main():
    n, l = read_input(task=1)

    n = int(n.strip())
    l = list(map(int, l.strip().split()))

    randomized_quick_sort(l, 0, n - 1)

    sl = (' '.join(map(str, l)))

    write_output(1, sl)
    print(sl)
    print()

if __name__ == '__main__':
    decorate(task=1, task_name='QuickSortPart3')