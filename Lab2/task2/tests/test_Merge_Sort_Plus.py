import unittest
import io
from Lab2.task2.src.Merge_Sort_Plus import *

class TestMergeSort(unittest.TestCase):

    def test_basic_sort_with_indices(self):
        array = [9, 7, 5, 8]
        output = io.StringIO()
        merge_sort(array, output)
        self.assertEqual(array, [9, 7, 5, 8])

    def test_already_sorted(self):
        array = [1, 2, 3, 4]
        output = io.StringIO()
        merge_sort(array, output)
        self.assertEqual(array, [1, 2, 3, 4])

    def test_reverse_sorted(self):
        array = [10, 9, 8, 7]
        output = io.StringIO()
        merge_sort(array, output)
        self.assertEqual(array, [10, 9, 8, 7])

    def test_single_element(self):
        array = [1]
        output = io.StringIO()
        merge_sort(array, output)
        self.assertEqual(array, [1])

    def test_empty_array(self):
        array = []
        output = io.StringIO()
        merge_sort(array, output)
        self.assertEqual(array, [])

if __name__ == '__main__':
    unittest.main()