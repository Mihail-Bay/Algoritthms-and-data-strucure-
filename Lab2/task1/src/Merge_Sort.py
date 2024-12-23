from Lab2.utils import read_input, write_output, decorate

def merge(left, right):
    r = []
    i = q = 0

    while i < len(left) and q < len(right):
        if left[i] < right[q]:
            r.append(left[i])
            i += 1
        else:
            r.append(right[q])
            q += 1

    r.extend(left[i:])
    r.extend(right[q:])
    return r

def merge_sort(l):
    if len(l) <= 1:
        return l

    mid = len(l) // 2
    left = merge_sort(l[:mid])
    right = merge_sort(l[mid:])
    return merge(left, right)

def main():
    n, l = read_input(task=1)
    sl = merge_sort(l)
    write_output(1, ' '.join(map(str, sl)))

if __name__ == '__main__':
    decorate(task=1, task_name='Merge_Sort')