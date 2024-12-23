
from Lab1.utils import read_input, write_output, decorate


def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - 1, i, -1):
            if arr[j] < arr[j - 1]:
                arr[j], arr[j - 1] = arr[j - 1], arr[j]
    return arr


def main():

    a = read_input(6)
    n = int(a[0])  # Читаем число элементов
    arr = list(map(int, a[1:]))  # Читаем массив из строки и преобразуем в список

    sorted_arr = bubble_sort(arr)  # Сортируем массив с помощью функции bubble_sort

    # Запись результата в файл
    write_output(6, ' '.join(map(str, sorted_arr)))

if __name__ == '__main__':
    decorate(task=1, task_name='task1')
