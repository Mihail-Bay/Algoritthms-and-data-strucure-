import time
import tracemalloc  # Импортируем модуль для отслеживания памяти

# Начинаем отслеживание использования памяти
tracemalloc.start()

t_start = time.perf_counter()  # Запоминаем начало времени выполнения


def merge_and_count(left, right):
    r = []  # Инициализируем пустой список для хранения отсортированных элементов
    i = q = 0  # Индексы для подмассивов left и right
    inversions_count = 0  # Счетчик инверсий

    # Проходим по обоим массивам, пока не достигнем конца одного из них
    while i < len(left) and q < len(right):
        if left[i] <= right[q]:  # Сравниваем текущие элементы
            r.append(left[i])  # Если элемент из left меньше, добавляем его в результат
            i += 1  # Переходим к следующему элементу в left
        else:
            # Здесь, если элемент из right меньше, значит, все оставшиеся элементы в left
            # образуют инверсии с текущим элементом right[j]
            inversions_count += len(left) - i  # Увеличиваем счетчик инверсий
            r.append(right[q])  # Добавляем элемент из right в результат
            q += 1  # Переходим к следующему элементу в right

    r.extend(left[i:])  # Добавляем оставшиеся элементы из left, если они есть
    r.extend(right[q:])  # Добавляем оставшиеся элементы из right, если они есть

    return r, inversions_count  # Возвращаем отсортированный массив и количество инверсий


def merge_sort_and_count(l):
    if len(l) <= 1:  # Если массив имеет 0 или 1 элемент
        return l, 0  # Возвращаем его и 0 инверсий

    mid = len(l) // 2  # Находим середину массива

    # Рекурсивно сортируем левую и правую половины и считаем инверсии
    left, left_inversions = merge_sort_and_count(l[:mid])
    right, right_inversions = merge_sort_and_count(l[mid:])

    # Сливаем отсортированные подмассивы и считаем инверсии при слиянии
    merged, split_inversions = merge_and_count(left, right)

    # Общее количество инверсий - инверсии в левой части + инверсии в правой части + инверсии при слиянии
    total_inversions = left_inversions + right_inversions + split_inversions

    return merged, total_inversions  # Возвращаем отсортированный массив и общее количество инверсий


if __name__ == '__main__':
    with open('../txtf/input.txt', 'r') as f:  # Открываем файл для чтения
        n = int(f.readline().strip())  # Читаем количество элементов в массиве
        l = list(map(int, f.readline().strip().split()))  # Читаем массив целых чисел


    sl, inversions = merge_sort_and_count(l)

    with open('../txtf/output.txt', 'w') as f:
        f.write(str(inversions))  # Записываем число инверсий

    # Вычисляем время выполнения
    elapsed_time = time.perf_counter() - t_start
    print(f"Время выполнения: {elapsed_time:.6f} секунд")

    # Получаем текущее использование памяти
    current, peak = tracemalloc.get_traced_memory()
    print(f"Текущая память: {current / 10**6:.6f} МБ; Пиковая память: {peak / 10**6:.6f} МБ")

    # Останавливаем отслеживание памяти
    tracemalloc.stop()