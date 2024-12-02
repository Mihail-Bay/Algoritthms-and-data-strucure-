import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Lab4.utils import read_input, write_output

def stack_commands(commands, n ):
    stack = []
    out = []
    for i in commands[1: n + 2]:
        if i[0] in '+-':
            if i[0] == '+':
                _, nuber = i.split()
                stack.append(nuber)
            elif i[0] == '-':
                if stack:
                    out.append(stack.pop())
    output = '\n'.join(out)
    return output

if __name__ == '__main__':
    commands = read_input(task=1)
    n = int(commands[0])
    out = stack_commands(commands, n)
    write_output(1, out)
