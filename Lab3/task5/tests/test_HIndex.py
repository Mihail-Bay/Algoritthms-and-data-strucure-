import unittest
from Lab3.task5.src.HIndex import *


class TestHIndexCalculation(unittest.TestCase):

    def test_single_value(self):
        self.assertEqual(Calculate_H_Index([0]), 0, "Single paper with 0 citations")
        self.assertEqual(Calculate_H_Index([5]), 1, "Single paper with 5 citations")

    def test_no_citations(self):
        self.assertEqual(Calculate_H_Index([0, 0, 0]), 0, "Multiple papers with 0 citations")

    def test_uniform_citations(self):
        self.assertEqual(Calculate_H_Index([1, 1, 1, 1]), 1, "All papers have 1 citation each")
        self.assertEqual(Calculate_H_Index([6, 6, 6, 6]), 4, "All papers have 6 citations each")

    def test_different_citations(self):
        self.assertEqual(Calculate_H_Index([3, 0, 6, 1, 5]), 3, "Varying citation counts")
        self.assertEqual(Calculate_H_Index([10, 8, 5, 4, 3]), 4, "Pre-sorted in descending order")

    def test_large_number_of_papers(self):
        citations = list(range(1, 101))  # 1 citation, 2 citations, ..., 100 citations
        self.assertEqual(Calculate_H_Index(citations), 50, "Consistent increase in citations")

    def test_descending_citations(self):
        self.assertEqual(Calculate_H_Index([5, 5, 5, 5, 5]), 5, "Multiple papers with equal citations")

# Running the tests
if __name__ == '__main__':
    unittest.main()