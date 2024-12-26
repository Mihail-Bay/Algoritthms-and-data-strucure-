from Lab1.utils import read_input, write_output, decorate


def isort(n, l):
    # Функция сортировки вставками
    lp = [1]  # Список, хранящий индексы вставок
    for i in range(1, n):
        for q in range(i - 1, -1, -1):
            if l[i] < l[q]:
                l[i], l[q] = l[q], l[i]  # Меняем местами
                i, q = q, i  # Обновляем индексы i и q
        lp.append(i + 1)  # Запоминаем позицию, куда вставили элемент

    return l, lp  # Возвращаем отсортированный список и позиции вставок

def main():
    # Читаем количество элементов из файла
    n = int(read_input(2)[0])

    # Читаем остальные элементы из файла и разбиваем на список целых чисел
    a = read_input(2)[1]  # Предполагаем, что числа находятся в первой строке после n
    l = list(map(int, a.split()))  # Преобразуем строку в список целых чисел



    # Сортируем список и получаем позицию вставок
    ls, lp = isort(n, l)

    # Преобразуем списки в строки для записи в выходной файл
    lps = ' '.join(map(str, lp))
    sl = ' '.join(map(str, ls))

    # Записываем результаты в выходной файл
    write_output(2, lps, sl)
    print(lps, sl)
    print()

if __name__ == '__main__':
    decorate(task=2, task_name='task2')
