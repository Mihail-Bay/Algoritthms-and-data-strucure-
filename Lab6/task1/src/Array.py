import os
import sys

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Lab6.utils import read_input, write_output, decorate  # Adjust this import if necessary


class CustomSet:
    def __init__(self):
        self.data = {}

    def add(self, x):
        """Добавление элемента в множество."""
        self.data[x] = True

    def remove(self, x):
        """Удаление элемента из множества."""
        if x in self.data:
            del self.data[x]

    def exists(self, x):
        """Проверка существования элемента в множестве."""
        return x in self.data


def main():
    # Читаем входные данные
    n = int(read_input(1)[0])  # Читаем количество операций
    operations = read_input(1)[1:n + 1]  # Читаем операции, начиная со второй строки

    custom_set = CustomSet()
    results = []

    for operation in operations:
        op_type, x = operation.split(' ')
        x = int(x)

        if op_type == 'A':
            custom_set.add(x)
        elif op_type == 'D':
            custom_set.remove(x)
        elif op_type == '?':
            results.append('Y' if custom_set.exists(x) else 'N')

    write_output(1, *results)  # Записываем результаты в выходной файл
    print('\n'.join(results) + '\n')


if __name__ == '__main__':
    decorate(task=1, task_name='Array')  # Передаем номер задачи и название модуля


