import time
import tracemalloc  # Импортируем модуль для отслеживания памяти

# Начинаем отслеживание использования памяти
tracemalloc.start()

t_start = time.perf_counter()  # Запоминаем начало времени выполнения


def merge(left, right, start_index, mid_index, end_index, output_file):
    r = []  # Список для хранения результата слияния
    i = q = 0    # Инициализация индексов для левой и правой части

    # Объединяем два массива, пока оба имеют элементы
    while i < len(left) and q < len(right):
        if left[i] < right[q]:  # Если текущий элемент левой части меньше
            r.append(left[i])  # Добавляем его в результат
            i += 1  # Переходим к следующему элементу левой части
        else:  # Если элемент правой части меньше или равен
            r.append(right[q])  # Добавляем его в результат
            q += 1  # Переходим к следующему элементу правой части

    # Добавляем оставшиеся элементы из левой части, если таковые есть
    r.extend(left[i:])
    # Добавляем оставшиеся элементы из правой части, если таковые есть
    r.extend(right[q:])

    # Запись индексов и значений в выходной файл
    if len(left) > 1 or len(right) > 1:  # Проверяем, чтобы записем только при необходимости
        output_file.write(str(f"{start_index} {mid_index} {r[0]} {r[-1]}\n"))

    return r  # Возвращаем отсортированный массив


def merge_sort(l, output_file, start_index=1):
    if len(l) <= 1:  # Если массив содержит 0 или 1 элемент, он уже отсортирован
        return l

    mid = len(l) // 2  # Нахождение середины массива
    # Рекурсивно сортируем левую половину
    left = merge_sort(l[:mid], output_file, start_index)
    # Рекурсивно сортируем правую половину
    right = merge_sort(l[mid:], output_file, start_index + mid)

    # Объединяем отсортированные половины и записываем результат
    return merge(left, right, start_index, start_index + mid - 1, start_index + len(l) - 1, output_file)

if __name__ == '__main__':
    # Чтение входных данных из файла
    with open('../txtf/input.txt', 'r') as f:
        n = int(f.readline().strip())  # Считываем количество элементов
        l = list(map(int, f.readline().strip().split()))  # Считываем массив чисел

    # Открытие выходного файла для записи
    with open('../txtf/output.txt', 'w') as f:
        # Выполнение сортировки и передача файла для записи
        sl = merge_sort(l, f)
        # Запись отсортированных данных в выходной файл
        f.write(' '.join(map(str, sl)))  # Записываем отсортированный массив в файл

    # Вычисляем время выполнения
    elapsed_time = time.perf_counter() - t_start
    print(f"Время выполнения: {elapsed_time:.6f} секунд")

    # Получаем текущее использование памяти
    current, peak = tracemalloc.get_traced_memory()
    print(f"Текущая память: {current / 10**6:.6f} МБ; Пиковая память: {peak / 10**6:.6f} МБ")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()