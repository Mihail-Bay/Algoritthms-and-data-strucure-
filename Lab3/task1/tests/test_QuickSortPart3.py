import unittest
from random import seed
from Lab3.task1.src.QuickSortPart3 import *

class TestQuickSort(unittest.TestCase):

    def test_sorted_array(self):
        l = [1, 2, 3, 4, 5]
        sorted_l = l[:]
        randomized_quick_sort(sorted_l, 0, len(sorted_l) - 1)
        self.assertEqual(sorted_l, sorted(l))

    def test_reverse_sorted_array(self):
        l = [5, 4, 3, 2, 1]
        sorted_l = l[:]
        randomized_quick_sort(sorted_l, 0, len(sorted_l) - 1)
        self.assertEqual(sorted_l, sorted(l))

    def test_random_array(self):
        l = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
        sorted_l = l[:]
        randomized_quick_sort(sorted_l, 0, len(sorted_l) - 1)
        self.assertEqual(sorted_l, sorted(l))

    def test_array_with_duplicates(self):
        l = [5, 5, 5, 5, 5]
        sorted_l = l[:]
        randomized_quick_sort(sorted_l, 0, len(sorted_l) - 1)
        self.assertEqual(sorted_l, sorted(l))

    def test_empty_array(self):
        l = []
        sorted_l = l[:]
        randomized_quick_sort(sorted_l, 0, len(sorted_l) - 1)
        self.assertEqual(sorted_l, [])

    def test_single_element_array(self):
        l = [1]
        sorted_l = l[:]
        randomized_quick_sort(sorted_l, 0, len(sorted_l) - 1)
        self.assertEqual(sorted_l, l)

    def test_large_array(self):
        seed(0)  # Устанавливаем seed для воспроизводимости
        l = [random.randint(1, 1000) for _ in range(1000)]
        sorted_l = l[:]
        randomized_quick_sort(sorted_l, 0, len(sorted_l) - 1)
        self.assertEqual(sorted_l, sorted(l))

if __name__ == '__main__':
    unittest.main()