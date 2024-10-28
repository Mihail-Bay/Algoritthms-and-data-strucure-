import unittest
from Lab2.task4.src.Binary_Search import *


class TestBinarySearch(unittest.TestCase):

    def test_element_present(self):
        self.assertEqual(binary_search([1, 5, 8, 12, 13], 8), 2)  # 8 присутствует
        self.assertEqual(binary_search([1, 5, 8, 12, 13], 1), 0)  # 1 - первое число
        self.assertEqual(binary_search([1, 5, 8, 12, 13], 13), 4)  # 13 - последнее число

    def test_element_absent(self):
        self.assertEqual(binary_search([1, 5, 8, 12, 13], 23), -1)  # 23 отсутствует
        self.assertEqual(binary_search([1, 5, 8, 12, 13], 0), -1)  # 0 меньше минимального

    def test_multiple_queries(self):
        sorted_list = [1, 5, 8, 12, 13]
        queries = [8, 1, 23, 1, 11]
        expected_results = [2, 0, -1, 0, -1]

        results = [binary_search(sorted_list, q) for q in queries]
        self.assertEqual(results, expected_results)

    def test_empty_list(self):
        self.assertEqual(binary_search([], 5), -1)  # Пустой массив


if __name__ == '__main__':
    unittest.main()