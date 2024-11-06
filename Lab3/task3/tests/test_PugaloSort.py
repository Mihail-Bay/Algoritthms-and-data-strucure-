import unittest
from Lab3.task3.src.PugaloSort import *


class TestCanSortMatriochkas(unittest.TestCase):

    def test_case1(self):
        n, k = 4, 2
        sizes = [3, 1, 4, 2]
        self.assertEqual(can_sort_matriochkas(n, k, sizes), "NO")

    def test_case2(self):
        n, k = 3, 1
        sizes = [3, 2, 1]
        self.assertEqual(can_sort_matriochkas(n, k, sizes), "YES")

    def test_case3(self):
        n, k = 5, 5
        sizes = [1, 2, 3, 4, 5]
        self.assertEqual(can_sort_matriochkas(n, k, sizes), "YES")

    def test_case4(self):
        n, k = 6, 3
        sizes = [4, 5, 6, 1, 2, 3]
        self.assertEqual(can_sort_matriochkas(n, k, sizes), "YES")

    def test_case5(self):
        n, k = 4, 2
        sizes = [4, 3, 2, 1]
        self.assertEqual(can_sort_matriochkas(n, k, sizes), "NO")

if __name__ == '__main__':
    unittest.main()