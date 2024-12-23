from Lab1.utils import read_input, write_output, decorate


def lin_ser(l, n):
    ind = []  # Список для хранения индексов, где найдено значение n
    for index, value in enumerate(l):
        if value == n:
            ind.append(index)  # Запоминаем индекс, если значение совпадает
    return len(ind), ind


def main():
    # Читаем строки из файла
    a = read_input(4)
    # Преобразуем строки в целые числа, разбивая строку на отдельные числа
    l = list(map(int, a[0].split()))  # Предполагаем, что все числа находятся в первой строке
    n = int(a[1])  # Значение n во второй строке
    # Вызов функции и присвоение результатов
    count, ind = lin_ser(l, n)

    lps = ', '.join(map(str, ind))  # Подготовка индексов к записи в файл
    sl = str(count) if count > 0 else "-1"  # Если значение не найдено, записываем -1
    write_output(4, sl, lps if count > 0 else "")


if __name__ == '__main__':
    decorate(task=4, task_name='task4')
