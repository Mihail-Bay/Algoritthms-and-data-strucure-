import unittest
from Lab1.Task2.src.task2 import isort
class TestTask2(unittest.TestCase):

    def test_sorted_list(self):
        l, lp = isort(5, [1, 2, 3, 4, 5])
        self.assertEqual(l, [1, 2, 3, 4, 5])
        self.assertEqual(lp, [1, 2, 3, 4, 5])

    def test_reverse_list(self):
        l, lp = isort(5, [5, 4, 3, 2, 1])
        self.assertEqual(l, [1, 2, 3, 4, 5])
        self.assertEqual(lp, [1, 1, 1, 1, 1])

    def test_unsorted_list(self):
        l, lp = isort(5, [3, 1, 4, 5, 2])
        self.assertEqual(l, [1, 2, 3, 4, 5])
        self.assertEqual(lp, [1, 1, 3, 4, 2])

    def test_empty_list(self):
        l, lp = isort(0, [])
        self.assertEqual(l, [])
        self.assertEqual(lp, [1])

    def test_single_element(self):
        l, lp = isort(1, [42])
        self.assertEqual(l, [42])
        self.assertEqual(lp, [1])

if __name__ == '__main__':
    unittest.main