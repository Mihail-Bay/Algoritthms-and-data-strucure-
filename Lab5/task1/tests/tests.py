import unittest
from Lab5.task1.src.Heap import Heap


class TestHoap(unittest.TestCase):

    def test_should_non_decreasing_heap(self):
        self.assertEqual(Heap([1, 2, 3, 4, 5], 5), "YES")
        self.assertEqual(Heap([1, 2, 1, 3, 2], 5), "YES")
        self.assertEqual(Heap([1, 1, 1, 1], 4), "YES")

    def test_should_not_a_heap(self):
        self.assertEqual(Heap([1, 3, 2, 4, 5], 5), "YES")
        self.assertEqual(Heap([5, 3, 2, 4, 1], 5), "NO")
        self.assertEqual(Heap([3, 2, 5, 1], 4), "NO")

    def test_should_single_element(self):
        self.assertEqual(Heap([1], 1), "YES")
        self.assertEqual(Heap([100], 1), "YES")

if __name__ == '__main__':
    unittest.main()