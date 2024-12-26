import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Lab5.utils import read_input, write_output, decorate


def Heap(l: int, ln: int):
    n = ln
    for i in range(1, n//2 + 1):
        one = 2 * i
        two = 2 * i + 1

        if one <= n:
            if l[i - 1] > l[one - 1]:
                return "NO"
        if two <= n:
            if l[i - 1] > l[two - 1]:
                return "NO"
    return "YES"


def main():
    lf = read_input(task=1)
    l = lf[1].split()
    ln = int(lf[0])
    out = Heap(l, ln)
    write_output(1, out)
    print(out)
    print()

if __name__ == '__main__':
    decorate(task=1,task_name='Heap')