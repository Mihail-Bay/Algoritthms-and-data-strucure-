from Lab1.utils import read_input, write_output, decorate


def opo_isort(l):
    # Функция сортировки вставками
    for i in range(1, len(l)):
        k = l[i]
        j = i - 1
        while j >= 0 and k > l[j]:  # Сравниваем с элементами списка
            l[j + 1] = l[j]  # Сдвигаем элемент l[j] на позицию l[j + 1]
            j -= 1  # Переходим к следующему элементу слева
        l[j + 1] = k  # Вставляем текущий элемент k на его правильную позицию

    return l

def main():
    # Читаем количество элементов из файла
    a = read_input(3)
    n = int(a[0])  # Читаем количество элементов
    l = list(map(int, a[1].split()))  # Преобразуем строку в список целых чисел



    # Сортируем список и формируем строку для записи в файл
    sl = ' '.join(map(str, opo_isort(l)))

    # Записываем отсортированные данные в файл
    write_output(3, sl)
    print(sl)
    print()

if __name__ == '__main__':
    decorate(task=3, task_name='task3')

