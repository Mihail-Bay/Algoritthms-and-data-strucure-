import unittest

from Lab1.Task1.src.task1 import isort
class TestTask1(unittest.TestCase):

    def test_empty_list(self):
        self.assertEqual(isort([]), [])

    def test_single_element_list(self):
        self.assertEqual(isort([1]), [1])

    def test_sorted_list(self):
        self.assertEqual(isort([1, 2, 3, 4, 5]), [1, 2, 3, 4, 5])

    def test_reverse_sorted_list(self):
        self.assertEqual(isort([5, 4, 3, 2, 1]), [1, 2, 3, 4, 5])

    def test_unsorted_list(self):
        self.assertEqual(isort([3, 1, 4, 5, 2]), [1, 2, 3, 4, 5])

    def test_list_with_duplicates(self):
        self.assertEqual(isort([2, 3, 3, 1, 5, 2]), [1, 2, 2, 3, 3, 5])

    def test_negative_numbers(self):
        self.assertEqual(isort([-3, -1, -7, 2, 0]), [-7, -3, -1, 0, 2])

    def test_mixed_numbers(self):
        self.assertEqual(isort([0, -2, 5, -1, 3, 5]), [-2, -1, 0, 3, 5, 5])


if __name__ == '__main__':
    unittest.main()