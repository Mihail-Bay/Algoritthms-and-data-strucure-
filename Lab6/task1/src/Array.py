import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Lab6.utils import read_input, write_output, decorate


class CustomSet:
    def __init__(self):
        self.data = {}

    def add(self, x):
        # Добавление элемента в множество
        self.data[x] = True

    def remove(self, x):
        # Удаление элемента из множества
        if x in self.data:
            del self.data[x]

    def exists(self, x):
        # Проверка существования элемента в множестве
        return x in self.data


def main():

    input_file = '../txtf/input.txt'
    output_file = '../txtf/output.txt'

    # Читаем входные данные
    with open(input_file, 'r') as f:
        n = int(f.readline().strip())
        operations = [f.readline().strip() for _ in range(n)]

    custom_set = CustomSet()
    results = []

    for operation in operations:
        op_type, x = operation.split()
        x = int(x)

        if op_type == 'A':
            custom_set.add(x)
        elif op_type == 'D':
            custom_set.remove(x)
        elif op_type == '?':
            if custom_set.exists(x):
                results.append('Y')
            else:
                results.append('N')

    # Записываем результаты в файл
    with open(output_file, 'w') as f:
        f.write('\n'.join(results) + '\n')


if __name__ == '__main__':
    decorate(task=1, task_name='Array')