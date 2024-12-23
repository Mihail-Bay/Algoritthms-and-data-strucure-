from Lab6.task7.src.Count_beautiful_pairs import *

import unittest


class TestCountBeautifulPairs(unittest.TestCase):

    def test_case_1(self):
        n, k = 7, 3
        S = "abacaba"
        beautiful_pairs = [
            ("a", "b"),
            ("a", "c"),
            ("b", "b"),
        ]
        result = count_beautiful_pairs(n, k, S, beautiful_pairs)
        self.assertEqual(result, 7)

    def test_case_2(self):
        n, k = 5, 2
        S = "abcde"
        beautiful_pairs = [
            ("a", "d"),
            ("b", "c"),
        ]
        result = count_beautiful_pairs(n, k, S, beautiful_pairs)
        self.assertEqual(result, 0)

if __name__ == '__main__':
    unittest.main()