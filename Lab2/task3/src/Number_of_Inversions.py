from Lab2.utils import read_input, write_output, decorate

def merge_and_count(left, right):
    r = []
    i = q = 0
    inversions_count = 0

    while i < len(left) and q < len(right):
        if left[i] <= right[q]:
            r.append(left[i])
            i += 1
        else:
            inversions_count += len(left) - i
            r.append(right[q])
            q += 1

    r.extend(left[i:])
    r.extend(right[q:])
    return r, inversions_count

def merge_sort_and_count(l):
    if len(l) <= 1:
        return l, 0

    mid = len(l) // 2
    left, left_inversions = merge_sort_and_count(l[:mid])
    right, right_inversions = merge_sort_and_count(l[mid:])
    merged, split_inversions = merge_and_count(left, right)

    total_inversions = left_inversions + right_inversions + split_inversions
    return merged, total_inversions

def main():
    n, l = read_input(task=3)
    sl, inversions = merge_sort_and_count(l)
    write_output(3, str(inversions))
    print(str(inversions))
    print()

if __name__ == '__main__':
    decorate(task=3, task_name='Number_of_Inversions')