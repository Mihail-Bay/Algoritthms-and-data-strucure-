from Lab2.utils import read_input, write_output, decorate

def binary_search(l, x):
    left, right = 0, len(l) - 1

    while left <= right:
        mid = (left + right) // 2
        if l[mid] == x:
            return mid
        elif l[mid] < x:
            left = mid + 1
        else:
            right = mid - 1

    return -1

def main():
    n, l, k, queries = read_input(task=4)
    r = []
    for q in queries:
        ind = binary_search(l, q)
        r.append(ind)

    write_output(4, ' '.join(map(str, r)))

if __name__ == '__main__':
    decorate(task=4, task_name='Binary_Search')