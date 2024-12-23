import unittest
from Lab1.Task5.src.task5 import sel_sort
class TestSelSort(unittest.TestCase):

    def test_sorted_array(self):
        l = [1, 2, 3, 4, 5]
        result = sel_sort(l.copy())
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        l = [5, 4, 3, 2, 1]
        result = sel_sort(l.copy())
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        l = [3, 1, 4, 5, 2]
        result = sel_sort(l.copy())
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_array_with_duplicates(self):
        l = [3, 1, 2, 1, 2]
        result = sel_sort(l.copy())
        self.assertEqual(result, [1, 1, 2, 2, 3])

    def test_empty_array(self):
        l = []
        result = sel_sort(l.copy())
        self.assertEqual(result, [])

    def test_single_element_array(self):
        l = [1]
        result = sel_sort(l.copy())
        self.assertEqual(result, [1])

if __name__ == '__main__':
    unittest.main()