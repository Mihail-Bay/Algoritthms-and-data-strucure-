from Lab6.task5.src.Process_elections import *

import unittest


class TestProcessElections(unittest.TestCase):


    def test_should_no_candidates(self):
        input_data = []
        expected_output = ""
        self.assertEqual(process_elections(input_data), expected_output)

    def test_should_invalid_vote_count(self):
        input_data = ["Alice ten"]
        with self.assertRaises(ValueError):
            process_elections(input_data)

if __name__ == '__main__':
    unittest.main()