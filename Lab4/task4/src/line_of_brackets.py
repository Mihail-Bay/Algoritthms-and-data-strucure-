import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Lab4.utils import read_input, write_output


def line_of_brackets(brackets):
    br = []
    for i in (str(brackets)):
        if str(brackets)[i] in '[]{}()':
            br.append((brackets[i], i))
    print(br)



if __name__ == '__main__':
    brackets = read_input(task=4)
    br = line_of_brackets(brackets)


