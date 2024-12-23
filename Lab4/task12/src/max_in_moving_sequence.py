import sys
import os
from Lab4.utils import read_input, write_output, decorate

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

class Queue:
    def __init__(self):
        self.input_file = read_input(12)

        # Проверяем, что входные данные корректны
        try:
            self.n = int(self.input_file[0])
            self.arr = list(map(int, self.input_file[1].split()))
            self.m = int(self.input_file[2])
        except ValueError as e:
            print(f"Ошибка при обработке входных данных: {e}")
            return  # Выход из конструктора, если данные некорректны

        self.queue = []
        self.max_queue = []  # Стек для хранения максимумов

    def pop(self):
        if self.queue:
            removed = self.queue.pop(0)
            if removed == self.max_queue[0]:
                self.max_queue.pop(0)  # Удаляем максимум из max_queue
            return removed
        return None

    def push(self, item):
        self.queue.append(item)
        # Обновляем max_queue
        while self.max_queue and self.max_queue[-1] < item:
            self.max_queue.pop()  # Удаляем все меньшие элементы из max_queue
        self.max_queue.append(item)

    def result(self):
        res = []
        for i in range(self.n):
            if len(self.queue) < self.m:
                self.push(self.arr[i])
            else:
                res.append(str(self.max_queue[0]))  # Записываем текущий максимум
                self.pop()  # Удаляем элемент
                self.push(self.arr[i])  # Добавляем новый элемент
        if len(self.queue) == self.m:  # Записываем максимум для последней группы
            res.append(str(self.max_queue[0]))
        return res

def main():
    q = Queue()
    res = q.result()
    write_output(12, ' '.join(res))
    print(*res)

if __name__ == "__main__":
    decorate(task=12, task_name="max_in_moving_sequence")