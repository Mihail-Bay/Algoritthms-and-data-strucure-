import unittest
from Lab1.Task6.src.task6 import bubble_sort
class TestBubbleSort(unittest.TestCase):

    def test_sorted_array(self):
        arr = [1, 2, 3, 4, 5]
        result = bubble_sort(arr.copy())
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_reverse_sorted_array(self):
        arr = [5, 4, 3, 2, 1]
        result = bubble_sort(arr.copy())
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_unsorted_array(self):
        arr = [3, 1, 4, 5, 2]
        result = bubble_sort(arr.copy())
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_single_element_array(self):
        arr = [1]
        result = bubble_sort(arr.copy())
        self.assertEqual(result, [1])

    def test_empty_array(self):
        arr = []
        result = bubble_sort(arr.copy())
        self.assertEqual(result, [])

    def test_identical_elements(self):
        arr = [2, 2, 2, 2, 2]
        result = bubble_sort(arr.copy())
        self.assertEqual(result, [2, 2, 2, 2, 2])

if __name__ == '__main__':
    unittest.main()