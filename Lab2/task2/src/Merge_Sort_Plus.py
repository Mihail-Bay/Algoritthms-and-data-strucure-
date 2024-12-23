from Lab2.utils import read_input, write_output, decorate

def merge(left, right, start_index, mid_index, end_index, output_file):
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

    if len(left) > 1 or len(right) > 1:
        output_file.write(f"{start_index} {mid_index} {r[0]} {r[-1]}\n")

    return r

def merge_sort(l, output_file, start_index=1):
    if len(l) <= 1:
        return l

    mid = len(l) // 2
    left = merge_sort(l[:mid], output_file, start_index)
    right = merge_sort(l[mid:], output_file, start_index + mid)
    return merge(left, right, start_index, start_index + mid - 1, start_index + len(l) - 1, output_file)

def main():
    n, l = read_input(task=2)

    # Открываем файл для записи
    with open('../txtf.output.txt', 'w') as f:
        sl = merge_sort(l, f)
        write_output(2, ' '.join(map(str, sl)))

if __name__ == '__main__':
    decorate(task=2, task_name='Merge_Sort_Plus')
