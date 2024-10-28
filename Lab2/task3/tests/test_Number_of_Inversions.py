import unittest
from Lab2.task3.src.Number_of_Inversions import *

class TestMergeSortAndCount(unittest.TestCase):

    def test_empty_array(self):
        result, inversions = merge_sort_and_count([])
        self.assertEqual(result, [])
        self.assertEqual(inversions, 0)

    def test_single_element_array(self):
        result, inversions = merge_sort_and_count([1])
        self.assertEqual(result, [1])
        self.assertEqual(inversions, 0)

    def test_sorted_array(self):
        result, inversions = merge_sort_and_count([1, 2, 3, 4, 5])
        self.assertEqual(result, [1, 2, 3, 4, 5])
        self.assertEqual(inversions, 0)

    def test_reverse_sorted_array(self):
        result, inversions = merge_sort_and_count([5, 4, 3, 2, 1])
        self.assertEqual(result, [1, 2, 3, 4, 5])
        self.assertEqual(inversions, 10)  # C(5, 2) = 10

    def test_array_with_repeats(self):
        result, inversions = merge_sort_and_count([1, 3, 2, 3, 1])
        self.assertEqual(result, [1, 1, 2, 3, 3])
        self.assertEqual(inversions, 4)  # (3, 2), (3, 1), (1, 2)

if __name__ == '__main__':
    unittest.main()