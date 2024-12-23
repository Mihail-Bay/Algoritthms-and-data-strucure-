import unittest
from Lab7.task4.src.longest_common_subsequence import longest_common_subsequence

class TestLongestCommonSubsequence(unittest.TestCase):

    def test_empty_sequences(self):
        self.assertEqual(longest_common_subsequence([], []), 0)

    def test_one_empty_sequence(self):
        self.assertEqual(longest_common_subsequence([], [1, 2, 3]), 0)
        self.assertEqual(longest_common_subsequence([1, 2, 3], []), 0)

    def test_no_common_elements(self):
        self.assertEqual(longest_common_subsequence([1, 2, 3], [4, 5, 6]), 0)

    def test_identical_sequences(self):
        self.assertEqual(longest_common_subsequence([1, 2, 3], [1, 2, 3]), 3)

    def test_partial_overlap(self):
        self.assertEqual(longest_common_subsequence([1, 2, 3, 4], [2, 4]), 2)
        self.assertEqual(longest_common_subsequence([1, 3, 4, 5], [1, 2, 3]), 2)

    def test_longer_sequences(self):
        self.assertEqual(longest_common_subsequence([1, 2, 3, 4, 5], [2, 3, 5, 6]), 3)
        self.assertEqual(longest_common_subsequence([1, 2, 3, 4, 5], [5, 4, 3, 2, 1]), 1)


if __name__ == '__main__':
    unittest.main()