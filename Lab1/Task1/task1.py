import time
import tracemalloc  # Импортируем модуль для отслеживания памяти

# Начинаем отслеживание использования памяти
tracemalloc.start()

t_start = time.perf_counter()  # Запоминаем начало времени выполнения

# Читаем количество элементов из файла
n = int(open('input.txt').readline())

# Читаем остальные элементы из файла и разделяем их на список строк
a = open('input.txt').read().split()

l = []  # Инициализируем список для хранения чисел
# Заполняем список l значениями, начиная с первой строки файла
if n != 0:
    for i in range(1, n+1):
        l.append(int(a[i]))  # Преобразуем строки в целые числа и добавляем в список

def isort(l):
    # Функция сортировки вставками
    for i in range(1, len(l)):
        s = l[i]  # Текущий элемент для вставки
        q = i - 1  # Индекс для проверки элементов слева от текущего
        # Сдвигаем элементы, которые больше текущего с места вставки
        while q >= 0 and s < l[q]:
            l[q + 1] = l[q]  # Сдвигаем элемент на одну позицию вправо
            q -= 1  # Переходим к следующему элементу слева
        l[q + 1] = s  # Вставляем текущий элемент на его место
    return l  # Возвращаем отсортированный список

# Применяем сортировку и формируем строку из отсортированных элементов
sl = (' '.join(map(str, isort(l))))

# Записываем отсортированные данные в файл
open('output.txt', 'w').write(sl)

# Вычисляем время выполнения
elapsed_time = time.perf_counter() - t_start
print(f"Время выполнения: {elapsed_time:.6f} секунд")

# Получаем текущее использование памяти
current, peak = tracemalloc.get_traced_memory()
print(f"Текущая память: {current / 10**6:.6f} МБ; Пиковая память: {peak / 10**6:.6f} МБ")

# Останавливаем отслеживание памяти
tracemalloc.stop()

import unittest
class TestTask1(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(isort([]), [])

    def test_single_element_list(self):
        self.assertEqual(isort([1]), [1])

    def test_sorted_list(self):
        self.assertEqual(isort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(isort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(isort([3, 1, 4, 5, 2]), [1, 2, 3, 4, 5])

    def test_list_with_duplicates(self):
        self.assertEqual(isort([2, 3, 3, 1, 5, 2]), [1, 2, 2, 3, 3, 5])

    def test_negative_numbers(self):
        self.assertEqual(isort([-3, -1, -7, 2, 0]), [-7, -3, -1, 0, 2])

    def test_mixed_numbers(self):
        self.assertEqual(isort([0, -2, 5, -1, 3, 5]), [-2, -1, 0, 3, 5, 5])


if __name__ == '__main__':
    unittest.main()