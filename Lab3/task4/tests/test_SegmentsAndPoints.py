import unittest
from Lab3.task4.src.SegmentsAndPonts import *


class TestCountSegments(unittest.TestCase):
    def test_basic_case(self):
        s = 2
        p = 3
        segments = [(0, 5), (7, 10)]
        points = [1, 6, 11]
        expected = [1, 0, 0]
        result = count_segments_containing_points(s, p, segments, points)
        self.assertEqual(result, expected)

    def test_all_points_covered(self):
        s = 1
        p = 3
        segments = [(0, 5)]
        points = [1, 2, 3]
        expected = [1, 1, 1]
        result = count_segments_containing_points(s, p, segments, points)
        self.assertEqual(result, expected)

    def test_no_segments(self):
        s = 0
        p = 3
        segments = []
        points = [1, 2, 3]
        expected = [0, 0, 0]
        result = count_segments_containing_points(s, p, segments, points)
        self.assertEqual(result, expected)

    def test_no_points(self):
        s = 2
        p = 0
        segments = [(0, 5), (7, 10)]
        points = []
        expected = []
        result = count_segments_containing_points(s, p, segments, points)
        self.assertEqual(result, expected)

    def test_points_on_edges(self):
        s = 2
        p = 2
        segments = [(0, 5), (5, 10)]
        points = [5, 10]
        expected = [2, 1]
        result = count_segments_containing_points(s, p, segments, points)
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()