from Lab2.utils import read_input, write_output, decorate

def majority_element(l):
    def find_c(l, left, right):
        if left == right:
            return l[left]

        mid = (left + right) // 2
        left_c = find_c(l, left, mid)
        right_c = find_c(l, mid + 1, right)

        if left_c == right_c:
            return left_c

        count_left = l[left:right + 1].count(left_c)
        count_right = l[left:right + 1].count(right_c)

        return left_c if count_left > count_right else right_c

    def count_occurrences(l, c):
        return l.count(c)

    n = len(l)
    c = find_c(l, 0, n - 1)

    if count_occurrences(l, c) > n // 2:
        return 1
    else:
        return 0

def main():
    n, l = read_input(task=5)
    r = majority_element(l)
    write_output(5, str(r))

if __name__ == '__main__':
    decorate(task=5, task_name='Delegate_Of_Majority')