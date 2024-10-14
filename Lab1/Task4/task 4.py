import time  # Импортируем модуль для отслеживания времени
import tracemalloc  # Импортируем модуль для отслеживания памяти

# Запускаем отслеживание использования памяти
tracemalloc.start()

t_start = time.perf_counter()  # Запоминаем время начала выполнения

# Читаем строки из файла и разбиваем их на список
a = open('input.txt').read().split()
l = []  # Инициализируем список для хранения чисел
# Заполняем список l целыми числами, считываемыми из файла
for i in range(0, len(a) - 1):
    l.append(int(a[i]))  # Преобразуем строки в целые числа
n = int(a[-1])  # Значение n во второй строке



def lin_ser(l, n):
    ind = []  # Список для хранения индексов, где найдено значение V

    # Проходим по всем элементам массива l и ищем значение V
    for index, value in enumerate(l):
        if value == n:
            ind.append(index)  # Запоминаем индекс, если значение совпадает

    # Возвращаем количество вхождений и индексы, даже если их нет
    return len(ind), ind

# Вызов функции и присвоение результатов
count, ind = lin_ser(l, n)

lps = ', '.join(map(str, ind))  # Подготовка индексов к записи в файл
sl = str(count) if count > 0 else "-1"  # Если значение не найдено, записываем -1

with open('output.txt', 'w') as file:
    file.write(sl + '\n')  # Записываем количество вхождений
    if count > 0:
        file.write(lps)  # Записываем индексы, если они есть

# Выводим время выполнения программы
elapsed_time = time.perf_counter() - t_start
print(f"Время выполнения: {elapsed_time:.6f} секунд")

# Получаем текущее использование памяти
current, peak = tracemalloc.get_traced_memory()
print(f"Текущая память: {current / 10**6:.6f} МБ; Пиковая память: {peak / 10**6:.6f} МБ")

# Останавливаем отслеживание использования памяти
tracemalloc.stop()


import unittest

class TestLinSer(unittest.TestCase):

    def test_multiple_occurrences(self):
        l = [1, 2, 3, 4, 3]
        n = 3
        count, ind = lin_ser(l, n)
        self.assertEqual(count, 2)
        self.assertEqual(ind, [2, 4])

    def test_single_occurrence(self):
        l = [5, 6, 7, 8]
        n = 6
        count, ind = lin_ser(l, n)
        self.assertEqual(count, 1)
        self.assertEqual(ind, [1])

    def test_no_occurrences(self):
        l = [9, 10, 11, 12]
        n = 15
        count, ind = lin_ser(l, n)
        self.assertEqual(count, 0)
        self.assertEqual(ind, [])

    def test_empty_list(self):
        l = []
        n = 1
        count, ind = lin_ser(l, n)
        self.assertEqual(count, 0)
        self.assertEqual(ind, [])

    def test_single_element_list(self):
        l = [2]
        n = 2
        count, ind = lin_ser(l, n)
        self.assertEqual(count, 1)
        self.assertEqual(ind, [0])

if __name__ == '__main__':
    unittest.main()