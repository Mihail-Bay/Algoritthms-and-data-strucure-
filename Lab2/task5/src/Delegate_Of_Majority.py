import time
import tracemalloc  # Импортируем модуль для отслеживания памяти

# Начинаем отслеживание использования памяти
tracemalloc.start()

t_start = time.perf_counter()  # Запоминаем начало времени выполнения


def majority_element(l):
    # Определяем функцию для нахождения элемента, который появляется более чем n/2 раз

    def find_c(l, left, right):
        # Вложенная функция для рекурсивного поиска кандидата на элемент большинства
        if left == right:
            # Если диапазон из одного элемента, возвращаем этот элемент
            return l[left]

        mid = (left + right) // 2  # Находим середину текущего диапазона

        # Рекурсивно ищем элементы большинства в левой и правой частях
        left_c = find_c(l, left, mid)
        right_c = find_c(l, mid + 1, right)

        if left_c == right_c:
            # Если оба элемента одинаковы, возвращаем их
            return left_c

        # Считаем количество вхождений каждого из кандидатов в текущем диапазоне
        count_left = l[left:right + 1].count(left_c)
        count_right = l[left:right + 1].count(right_c)

        # Возвращаем того кандидата, который встречается чаще
        return left_c if count_left > count_right else right_c

    def count_occurrences(l, c):
        # Вложенная функция для подсчета вхождений элемента c в массиве l
        return l.count(c)

    n = len(l)  # Сохраняем длину массива
    c = find_c(l, 0, n - 1)  # Ищем кандидата на элемент большинства

    # Проверяем, является ли найденный элемент элементом большинства
    if count_occurrences(l, c) > n // 2:
        return 1  # Если найденный элемент является элементом большинства, возвращаем 1
    else:
        return 0  # Если нет, возвращаем 0


if __name__ == '__main__':
    # Чтение входного файла
    with open('../txtf/input.txt', 'r') as f:
        n = int(f.readline().strip())  # Читаем размер массива
        l = list(map(int, f.readline().strip().split()))  # Читаем массив и преобразуем строки в целые числа

    # Вызываем функцию и записываем результат в выходной файл
    r = majority_element(l)

    with open('../txtf/output.txt', 'w') as f_out:
        f_out.write(str(r))  # Записываем результат работы функции в файл

    # Вычисляем время выполнения
    elapsed_time = time.perf_counter() - t_start
    print(f"Время выполнения: {elapsed_time:.6f} секунд")

    # Получаем текущее использование памяти
    current, peak = tracemalloc.get_traced_memory()
    print(f"Текущая память: {current / 10**6:.6f} МБ; Пиковая память: {peak / 10**6:.6f} МБ")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()