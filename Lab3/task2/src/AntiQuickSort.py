import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Lab3.utils import read_input, write_output, decorate


def generate_max_comparisons_test(n):
    # Создаем отсортированный массив
    test_array = list(range(1, n + 1))
    return test_array

def main():
    n = read_input(task=2)

    n = int(n[0])

    test_array = generate_max_comparisons_test(n)
    test_array = (' '.join(map(str, test_array)))

    write_output(2, test_array)
    print(test_array)
    print()


if __name__ == '__main__':
    decorate(task=2, task_name='AntiQuickSort')