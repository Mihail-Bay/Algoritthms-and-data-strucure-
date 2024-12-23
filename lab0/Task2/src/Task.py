
from lab0.utils import read_input, write_output, decorate

def main():


    f1 = 1
    f2 = 1
    i = 0

    n = int(read_input(2)[0])

    if n == 0:
        write_output(2, str(0))
    elif n == 1 or n == 2:
        write_output(2, str(1))
    elif 0 <= n <= 10**7 + 1:
        while i < n - 2:
            f_s = f1 + f2
            f1 = f2 % 10
            f2 = f_s % 10
            i += 1
        write_output(2, str(f_s % 10))
    else:
        print('Error')

if __name__ == "__main__":
    decorate(task=2, task_name='Task')

