from lab0.utils import read_input, write_output, decorate


def main():
    num = read_input(5)[0]
    splitnum = num.split()

    if -10 ** 9 <= int(splitnum[0]) <= 10 ** 9 + 1 and -10 ** 9 <= int(splitnum[1]) <= 10 ** 9 + 1:
        a = int(splitnum[0]) + int(splitnum[1])
        write_output(5, str(a))
    else:
        print('Error')


if __name__ == "__main__":
    decorate(task=5, task_name='Task')