import unittest
from Lab1.Task3.src.task3 import opo_isort
class TestDescendingInsertionSort(unittest.TestCase):

    def test_sorted_list(self):
        l = [1, 2, 3, 4, 5]
        sorted_l = opo_isort(l.copy())
        self.assertEqual(sorted_l, [5, 4, 3, 2, 1])

    def test_reverse_list(self):
        l = [5, 4, 3, 2, 1]
        sorted_l = opo_isort(l.copy())
        self.assertEqual(sorted_l, [5, 4, 3, 2, 1])

    def test_mixed_list(self):
        l = [3, 1, 4, 2, 5]
        sorted_l = opo_isort(l.copy())
        self.assertEqual(sorted_l, [5, 4, 3, 2, 1])

    def test_all_equal_elements(self):
        l = [2, 2, 2, 2, 2]
        sorted_l = opo_isort(l.copy())
        self.assertEqual(sorted_l, [2, 2, 2, 2, 2])

    def test_single_element(self):
        l = [1]
        sorted_l = opo_isort(l.copy())
        self.assertEqual(sorted_l, [1])

    def test_empty_list(self):
        l = []
        sorted_l = opo_isort(l.copy())
        self.assertEqual(sorted_l, [])

if __name__ == '__main__':
    unittest.main()