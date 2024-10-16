import time # импортируем модуль для отслеживания времени
import tracemalloc  # Импортируем модуль для отслеживания памяти

# Запускаем отслеживание использования памяти
tracemalloc.start()

t_start = time.perf_counter()  # Запоминаем время начала выполнения

# Читаем количество элементов из файла
n = int(open('input.txt').readline())

# Читаем строки из файла и разбиваем их на список
a = open('input.txt').read().split()

l = []  # Инициализируем список для хранения чисел

# Заполняем список l целыми числами, считываемыми из файла
for i in range(1, n + 1):
    l.append(int(a[i]))  # Преобразуем строки в целые числа

def isort(n, l):
    # Функция сортировки вставками
    lp = [1]  # Список, хранящий индексы вставок
    # Проходим по элементам списка, начиная со второго
    for i in range(1, n):
        # Для текущего элемента проверяем все предыдущие
        for q in range(i - 1, -1, -1):
            # Если текущий элемент меньше, чем элемент на позиции q
            if l[i] < l[q]:
                l[i], l[q] = l[q], l[i]  # Меняем местами
                i, q = q, i  # Обновляем индексы i и q
        lp.append(i + 1)  # Запоминаем позицию, куда вставили элемент

    return l, lp  # Возвращаем отсортированный список и позиции вставок

# Сортируем список и получаем позицию вставок
ls, lp = isort(n, l)

# Преобразуем списки в строки для записи в выходной файл
lps = ' '.join(map(str, lp))
sl = ' '.join(map(str, ls))

# Записываем результаты в выходной файл
with open('output.txt', 'w') as file:
    file.write(lps + '\n')  # Записываем позиции вставок
    file.write(sl)          # Записываем отсортированный список

# Выводим время выполнения программы
elapsed_time = time.perf_counter() - t_start
print(f"Время выполнения: {elapsed_time:.6f} секунд")

# Получаем текущее использование памяти
current, peak = tracemalloc.get_traced_memory()
print(f"Текущая память: {current / 10**6:.6f} МБ; Пиковая память: {peak / 10**6:.6f} МБ")

# Останавливаем отслеживание использования памяти
tracemalloc.stop()

import unittest
class TestTask2(unittest.TestCase):

    def test_sorted_list(self):
        l, lp = isort(5, [1, 2, 3, 4, 5])
        self.assertEqual(l, [1, 2, 3, 4, 5])
        self.assertEqual(lp, [1, 2, 3, 4, 5])

    def test_reverse_list(self):
        l, lp = isort(5, [5, 4, 3, 2, 1])
        self.assertEqual(l, [1, 2, 3, 4, 5])
        self.assertEqual(lp, [1, 1, 1, 1, 1])

    def test_unsorted_list(self):
        l, lp = isort(5, [3, 1, 4, 5, 2])
        self.assertEqual(l, [1, 2, 3, 4, 5])
        self.assertEqual(lp, [1, 1, 3, 4, 2])

    def test_empty_list(self):
        l, lp = isort(0, [])
        self.assertEqual(l, [])
        self.assertEqual(lp, [1])

    def test_single_element(self):
        l, lp = isort(1, [42])
        self.assertEqual(l, [42])
        self.assertEqual(lp, [1])

if __name__ == '__main__':
    unittest.main
