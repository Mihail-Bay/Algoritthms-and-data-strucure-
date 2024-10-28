import unittest
from Lab2.task1.src.Merge_Sort import *


class TestMergeSort(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(merge_sort([]), [])

    def test_single_element(self):
        self.assertEqual(merge_sort([1]), [1])
        self.assertEqual(merge_sort([-1]), [-1])

    def test_sorted_list(self):
        self.assertEqual(merge_sort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(merge_sort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(merge_sort([3, 2, 5, 4, 1]), [1, 2, 3, 4, 5])

    def test_duplicates(self):
        self.assertEqual(merge_sort([1, 2, 2, 3, 1]), [1, 1, 2, 2, 3])

    def test_large_numbers(self):
        self.assertEqual(merge_sort([1000, 500, 300, 800]), [300, 500, 800, 1000])

    def test_negative_numbers(self):
        self.assertEqual(merge_sort([-1, -2, 0, 2, 1]), [-2, -1, 0, 1, 2])


if __name__ == '__main__':
    unittest.main()