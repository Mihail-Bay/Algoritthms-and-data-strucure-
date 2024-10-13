import time  # Импортируем модуль для отслеживания времени
import tracemalloc  # Импортируем модуль для отслеживания памяти

# Запускаем отслеживание использования памяти
tracemalloc.start()

t_start = time.perf_counter()  # Запоминаем время начала выполнения


def bubble_sort(arr):

    n = len(arr)  # Определяем размер массива
    for i in range(n):  # Проходим по каждому элементу
        # Внешний цикл отвечает за количество проходов по массиву
        for j in range(n - 1, i, -1):  # Обратный порядок нам нужен для сравнения пар
            # Если текущий элемент больше следующего, меняем их местами
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr  # Возвращаем отсортированный массив


def main():
    # Чтение данных из файла
    with open('input.txt', 'r') as file:
        n = int(file.readline().strip())  # Читаем число элементов
        arr = list(map(int, file.readline().strip().split()))  # Читаем массив из строки и преобразуем в список

    sorted_arr = bubble_sort(arr)  # Сортируем массив с помощью функции bubble_sort

    # Запись результата в файл
    with open('output.txt', 'w') as file:
        file.write(' '.join(map(str, sorted_arr)))  # Записываем отсортированный массив в файл


if __name__ == "__main__":
    main()  # Запускаем основную функцию


# Вычисляем время выполнения
elapsed_time = time.perf_counter() - t_start
print(f"Время выполнения: {elapsed_time:.6f} секунд")

# Получаем текущее использование памяти
current, peak = tracemalloc.get_traced_memory()
print(f"Текущая память: {current / 10**6:.6f} МБ; Пиковая память: {peak / 10**6:.6f} МБ")

# Останавливаем отслеживание памяти
tracemalloc.stop()