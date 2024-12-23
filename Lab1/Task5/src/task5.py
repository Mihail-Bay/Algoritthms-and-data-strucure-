
from Lab1.utils import read_input, write_output, decorate


def sel_sort(l):
    n = len(l)
    for i in range(n):
        min_index = i  # Инициализируем индекс наименьшего элемента
        for j in range(i + 1, n):
            if l[j] < l[min_index]:  # Если найден меньший элемент
                min_index = j  # Обновляем индекс наименьшего элемента
        l[i], l[min_index] = l[min_index], l[i]  # Меняем местами
    return l


def main():



    # Чтение данных из файла
    a = read_input(5)
    n = int(a[0])  # Читаем число элементов
    l = list(map(int, a[1:]))  # Читаем массив из строки и преобразуем в список

    sl = sel_sort(l)  # Сортируем массив с помощью функции selection_sort

    # Запись результата в файл
    write_output(5, ' '.join(map(str, sl)))

if __name__ == '__main__':
    decorate(task=1, task_name='task1')
