import time  # Импортируем модуль для отслеживания времени
import tracemalloc  # Импортируем модуль для отслеживания памяти

# Запускаем отслеживание использования памяти
tracemalloc.start()

t_start = time.perf_counter()  # Запоминаем время начала выполнения

# Читаем количество элементов из файла
with open('input.txt') as file:
    n = int(file.readline())  # Читаем количество элементов
    a = file.read().split()  # Читаем оставшуюся часть файла и разбиваем на строки

l = []  # Инициализируем список для хранения чисел

# Заполняем список l целыми числами
for i in range(n):
    l.append(int(a[i]))  # Преобразуем строки в целые числа


def opo_isort(l):
    # Функция сортировки вставками
    # Проходим по всем элементам списка, начиная со второго
    for i in range(1, len(l)):
        # Сохраняем текущий элемент в переменной k
        k = l[i]
        # Устанавливаем индекс j на один элемент перед i
        j = i - 1

        while j >= 0 and k > l[j]:  # Сравниваем с элементами списка
            l[j + 1] = l[j]  # Сдвигаем элемент l[j] на позицию l[j + 1]
            j -= 1  # Переходим к следующему элементу слева

        # Вставляем текущий элемент k на его правильную позицию
        l[j + 1] = k

        # Возвращаем отсортированный список
    return l

# Сортируем список и формируем строку для записи в файл
sl = ' '.join(map(str, opo_isort(l)))

# Записываем отсортированные данные в файл
with open('output.txt', 'w') as file:
    file.write(sl)

# Вычисляем время выполнения
elapsed_time = time.perf_counter() - t_start
print(f"Время выполнения: {elapsed_time:.6f} секунд")

# Получаем текущее использование памяти
current, peak = tracemalloc.get_traced_memory()
print(f"Текущая память: {current / 10**6:.6f} МБ; Пиковая память: {peak / 10**6:.6f} МБ")

# Останавливаем отслеживание памяти
tracemalloc.stop()


import unittest

class TestDescendingInsertionSort(unittest.TestCase):

    def test_sorted_list(self):
        l = [1, 2, 3, 4, 5]
        sorted_l = opo_isort(l.copy())
        self.assertEqual(sorted_l, [5, 4, 3, 2, 1])

    def test_reverse_list(self):
        l = [5, 4, 3, 2, 1]
        sorted_l = opo_isort(l.copy())
        self.assertEqual(sorted_l, [5, 4, 3, 2, 1])

    def test_mixed_list(self):
        l = [3, 1, 4, 2, 5]
        sorted_l = opo_isort(l.copy())
        self.assertEqual(sorted_l, [5, 4, 3, 2, 1])

    def test_all_equal_elements(self):
        l = [2, 2, 2, 2, 2]
        sorted_l = opo_isort(l.copy())
        self.assertEqual(sorted_l, [2, 2, 2, 2, 2])

    def test_single_element(self):
        l = [1]
        sorted_l = opo_isort(l.copy())
        self.assertEqual(sorted_l, [1])

    def test_empty_list(self):
        l = []
        sorted_l = opo_isort(l.copy())
        self.assertEqual(sorted_l, [])

if __name__ == '__main__':
    unittest.main()