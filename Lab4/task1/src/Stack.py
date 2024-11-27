from Lab4.utils import read_input, write_output

def stack_comands(task):
    commands = read_input(task)
    n = int(commands[0])
    stack = []
    out = []
    for i in commands[1: n + 1]:
        if i[0] == '+':
            _, nuber = i.split()
            stack.append(nuber)
        elif i[0] == '-':
            if stack:
                out.append(stack.pop())
    output = '\n'.join(out)
    write_output(task, output)

if __name__ == '__main__':
    stack_comands(task=1)