from lab0.utils import read_input, write_output, decorate

def main():

    f1 = 1
    f2 = 1
    i = 0

    n = int(read_input(1)[0])
    if n == 0:
        write_output(1, str(0))
    elif n == 1 or n == 2:
        write_output(1, str(1))
    elif 0 <= n <= 45:
        while i < n - 2:
            f_s = f1 + f2
            f1 = f2
            f2 = f_s
            i += 1
        write_output(1, str(f_s))
    else:
        print('Error')


if __name__ == "__main__":
    decorate(task=1, task_name='Task')