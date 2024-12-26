
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from Lab3.utils import read_input, write_output, decorate



def count_segments_containing_points(s, p, segments, points):
    # Список событий
    events = []

    # Добавляем сегменты
    for i, (a, b) in enumerate(segments):
        events.append((a, 'L', i))  # L - левая граница отрезка
        events.append((b, 'R', i))  # R - правая граница отрезка

    # Добавляем точки
    for i, x in enumerate(points):
        events.append((x, 'P', i))  # P - точка

    # Сортируем события
    events.sort(key=lambda event: (event[0], event[1]))

    # Массив для результатов
    results = [0] * p
    active_segments = 0

    # Обработка событий
    for event in events:
        if event[1] == 'L':
            # Начало отрезка
            active_segments += 1
        elif event[1] == 'R':
            # Конец отрезка
            active_segments -= 1
        elif event[1] == 'P':
            # Точка
            point_index = event[2]
            results[point_index] = active_segments

    return results


# Чтение входных данных
def main():
    l = read_input(task=4)
    s, p = map(int, l[0].split())
    segments = [tuple(map(int, l[_ + 1].split())) for _ in range(s)]
    points = list(map(int, l[s+1].split()))

    res = count_segments_containing_points(s, p, segments, points)

    res = (" ".join(map(str, res)) + "\n")
    write_output(4, res)
    print(res)
    print()

if __name__ == "__main__":
    decorate(task=4, task_name='SegmentsAndPonts')