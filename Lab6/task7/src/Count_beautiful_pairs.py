from collections import defaultdict


from Lab6.utils import read_input, write_output, decorate


def count_beautiful_pairs(n, k, S, beautiful_pairs):
    pair_map = defaultdict(list)

    # Создание отображения для красивых пар
    for a, b in beautiful_pairs:
        pair_map[a].append(b)

    # Словарь для подсчета встречаемости камней
    count = defaultdict(int)
    beautiful_pair_count = 0

    # Проход по каждому камню в строке S
    for stone in S:
        if stone in pair_map:  # Если это 'a' из пары (a, b)
            for b in pair_map[stone]:  # Получаем 'b' для текущего 'a'
                # Увеличиваем количество красивых пар на количество уже встреченных 'b'
                beautiful_pair_count += count[b]

                # Увеличиваем счетчик текущего камня
        count[stone] += 1

    return beautiful_pair_count


def main():
    input_data = read_input(7)
    n, k = map(int, input_data[0].strip().split())
    S = input_data[1].strip()

    beautiful_pairs = []
    for i in range(2, 2 + k):
        pair = input_data[i].strip().split()
        if len(pair) == 2:  # Убедимся, что пара корректная
            beautiful_pairs.append(pair)
        else:
            print(f"Неверная пара: {pair}, ожидается пара из двух элементов.")

    result = count_beautiful_pairs(n, k, S, beautiful_pairs)

    write_output(7, result)


if __name__ == '__main__':
    decorate(task=7, task_name='Count_beautiful_pairs')
