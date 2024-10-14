import time  # Импортируем модуль для отслеживания времени
import tracemalloc  # Импортируем модуль для отслеживания памяти

# Запускаем отслеживание использования памяти
tracemalloc.start()

t_start = time.perf_counter()  # Запоминаем время начала выполнения


def sel_sort(l):
    n = len(l)  # Определяем размер массива
    for i in range(n):  # Проходим по каждому элементу массива
        # Предполагаем, что текущий элемент — наименьший
        min_index = i  # Инициализируем индекс наименьшего элемента
        # Вложенный цикл для поиска наименьшего элемента в оставшейся части массива
        for j in range(i + 1, n):
            if l[j] < l[min_index]:  # Если найден меньший элемент
                min_index = j  # Обновляем индекс наименьшего элемента
        # Меняем местами найденный наименьший элемент с i-м элементом
        l[i], l[min_index] = l[min_index], l[i]
    return l  # Возвращаем отсортированный массив



# Чтение данных из файла
with open('input.txt', 'r') as file:
    n = int(file.readline().strip())  # Читаем число элементов
    l = list(map(int, file.readline().strip().split()))  # Читаем массив из строки и преобразуем в список

sl = sel_sort(l)  # Сортируем массив с помощью функции selection_sort

# Запись результата в файл
with open('output.txt', 'w') as file:
    file.write(' '.join(map(str, sl)))  # Записываем отсортированный массив в файл





# Выводим время выполнения программы
elapsed_time = time.perf_counter() - t_start
print(f"Время выполнения: {elapsed_time:.6f} секунд")

# Получаем текущее использование памяти
current, peak = tracemalloc.get_traced_memory()
print(f"Текущая память: {current / 10**6:.6f} МБ; Пиковая память: {peak / 10**6:.6f} МБ")

# Останавливаем отслеживание использования памяти
tracemalloc.stop()

import unittest

class TestSelSort(unittest.TestCase):

    def test_sorted_array(self):
        l = [1, 2, 3, 4, 5]
        result = sel_sort(l.copy())
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        l = [5, 4, 3, 2, 1]
        result = sel_sort(l.copy())
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        l = [3, 1, 4, 5, 2]
        result = sel_sort(l.copy())
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_array_with_duplicates(self):
        l = [3, 1, 2, 1, 2]
        result = sel_sort(l.copy())
        self.assertEqual(result, [1, 1, 2, 2, 3])

    def test_empty_array(self):
        l = []
        result = sel_sort(l.copy())
        self.assertEqual(result, [])

    def test_single_element_array(self):
        l = [1]
        result = sel_sort(l.copy())
        self.assertEqual(result, [1])

if __name__ == '__main__':
    unittest.main()