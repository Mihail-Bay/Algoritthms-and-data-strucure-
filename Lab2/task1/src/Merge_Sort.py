import time
import tracemalloc  # Импортируем модуль для отслеживания памяти

# Начинаем отслеживание использования памяти
tracemalloc.start()

t_start = time.perf_counter()  # Запоминаем начало времени выполнения

# Функция для слияния двух отсортированных массивов
def merge(left, right):
    r = []  # Инициализация пустого списка для хранения результата слияния
    i = q = 0    # Индексы для текущих элементов левого и правого массивов

    # Объединяем два массива, пока есть элементы в обоих
    while i < len(left) and q < len(right):
        if left[i] < right[q]:  # Если элемент из левой части меньше элемента из правой
            r.append(left[i])  # Добавляем его в результат
            i += 1  # Переходим к следующему элементу в левой части
        else:  # Если элемент из правой части меньше или равен
            r.append(right[q])  # Добавляем его в результат
            q += 1  # Переходим к следующему элементу в правой части

    # Копируем оставшиеся элементы из левой части, если они есть
    r.extend(left[i:])
    # Копируем оставшиеся элементы из правой части, если они есть
    r.extend(right[q:])

    return r  # Возвращаем отсортированный массив, объединенный из двух частей


# Функция сортировки слиянием
def merge_sort(l):
    if len(l) <= 1:  # Если массив содержит 0 или 1 элемент, он уже отсортирован
        return l

    mid = len(l) // 2  # Находим середину массива
    # Рекурсивно сортируем левую половину массива
    left = merge_sort(l[:mid])
    # Рекурсивно сортируем правую половину массива
    right = merge_sort(l[mid:])

    # Объединяем отсортированные половины
    return merge(left, right)


if __name__ == '__main__':
    # Открываем файл "input.txt" для чтения
    with open('../txtf/input.txt', 'r') as f:
        n = int(f.readline().strip())  # Читаем количество элементов (первую строку) и преобразуем в целое число
        # Читаем вторую строку, разбиваем на числа и преобразуем в список целых чисел
        l = list(map(int, f.readline().strip().split()))

    # Сортировка массива с помощью функции merge_sort
    sl = merge_sort(l)

    # Открываем файл "output.txt" для записи
    with open('../txtf/output.txt', 'w') as f:
        # Записываем отсортированный массив в файл в виде строки
        f.write(' '.join(map(str, sl)))

    # Вычисляем время выполнения
    elapsed_time = time.perf_counter() - t_start
    print(f"Время выполнения: {elapsed_time:.6f} секунд")

    # Получаем текущее использование памяти
    current, peak = tracemalloc.get_traced_memory()
    print(f"Текущая память: {current / 10 ** 6:.6f} МБ; Пиковая память: {peak / 10 ** 6:.6f} МБ")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()