import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Lab3.utils import read_input, write_output, decorate


def Calculate_H_Index(citations):
    citations.sort(reverse=True)

    I_counter = 0

    for i in range(len(citations)):
        if citations[i] >= i + 1:
            I_counter = i + 1
        else:
            break

    return I_counter


def main():
    lines = read_input(task=5)  # Получаем список строк
    combined_str = ' '.join(lines)  # Объединяем строки в одну строку

    # Преобразуем объединенную строку в список чисел
    citations = list(map(int, combined_str.split()))

    res = Calculate_H_Index(citations)
    write_output(5, res )  # Указываем task при записи
    print(res)
    print()

if __name__ == '__main__':
    decorate(task=5, task_name='HIndex')