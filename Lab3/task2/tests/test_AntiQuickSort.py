import unittest
from Lab3.task2.src.AntiQuickSort import *

class TestGenerateMaxComparisonsTest(unittest.TestCase):
    def test_sorted_array_generation(self):
        # Test with small n
        result = generate_max_comparisons_test(5)
        self.assertEqual(result, [1, 2, 3, 4, 5])

        # Test with zero n
        result = generate_max_comparisons_test(0)
        self.assertEqual(result, [])

        # Test with large n
        n = 100
        result = generate_max_comparisons_test(n)
        self.assertEqual(result, list(range(1, n + 1)))

    def test_output_format(self):
        # Test the conversion to string format for output
        n = 5
        test_array = generate_max_comparisons_test(n)
        test_array_str = ' '.join(map(str, test_array))
        self.assertEqual(test_array_str, '1 2 3 4 5')


if __name__ == '__main__':
    unittest.main()