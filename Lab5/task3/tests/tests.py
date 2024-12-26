from Lab5.task3.src.network_packet import *

import unittest

class TestNetworkPacketsProcessor(unittest.TestCase):

    def setUp(self):
        # Prepare test data for the NetworkPacketsProcessor
        self.processor = NetworkPacketsProcessor()
        # Override the input data for testing purposes
        self.processor.buffer_size = 2
        self.processor.n = 5
        self.processor.packets = [
            [0, 3],  # Packet 1: arrival time 0, processing time 3
            [1, 9],  # Packet 2: arrival time 1, processing time 9
            [2, 6],  # Packet 3: arrival time 2, processing time 6
            [3, 4],  # Packet 4: arrival time 3, processing time 4
            [4, 5],  # Packet 5: arrival time 4, processing time 5
        ]
        self.processor.buffer = []
        self.processor.start_times = []


    def test_buffer_limit(self):
        self.processor.buffer_size = 1  # Set buffer size to 1
        self.processor.packets = [
            [0, 3],  # Packet 1: arrival time 0, processing time 3
            [1, 1],  # Packet 2: arrival time 1, processing time 1
            [2, 1],  # Packet 3: arrival time 2, processing time 1
        ]
        expected_results = ['0', '-1', '-1']  # Only first packet can be processed
        results = self.processor.network_packets(self.processor.buffer_size, self.processor.packets, len(self.processor.packets))
        self.assertEqual(results, expected_results)

if __name__ == '__main__':
    unittest.main()