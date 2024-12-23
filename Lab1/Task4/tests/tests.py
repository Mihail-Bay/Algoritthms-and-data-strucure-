import unittest
from Lab1.Task4.src.task4 import lin_ser
class TestLinSer(unittest.TestCase):

    def test_multiple_occurrences(self):
        l = [1, 2, 3, 4, 3]
        n = 3
        count, ind = lin_ser(l, n)
        self.assertEqual(count, 2)
        self.assertEqual(ind, [2, 4])

    def test_single_occurrence(self):
        l = [5, 6, 7, 8]
        n = 6
        count, ind = lin_ser(l, n)
        self.assertEqual(count, 1)
        self.assertEqual(ind, [1])

    def test_no_occurrences(self):
        l = [9, 10, 11, 12]
        n = 15
        count, ind = lin_ser(l, n)
        self.assertEqual(count, 0)
        self.assertEqual(ind, [])

    def test_empty_list(self):
        l = []
        n = 1
        count, ind = lin_ser(l, n)
        self.assertEqual(count, 0)
        self.assertEqual(ind, [])

    def test_single_element_list(self):
        l = [2]
        n = 2
        count, ind = lin_ser(l, n)
        self.assertEqual(count, 1)
        self.assertEqual(ind, [0])

if __name__ == '__main__':
    unittest.main()