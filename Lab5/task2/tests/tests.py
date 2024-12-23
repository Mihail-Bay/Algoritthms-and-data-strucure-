import unittest
from Lab4.task1.src.Stack import stack_commands


class TestStackCommands(unittest.TestCase):

    def test_should_stack_commands(self):
        self.assertEqual(stack_commands(['5', '+ 1', '+ 2', '-', '+ 3', '-'], 5), '2\n3')

    def test_should_only_pops(self):
        self.assertEqual(stack_commands(['4', '-', '-', '-'], 4), '')

    def test_should_more_pushes_than_pops(self):
        self.assertEqual(stack_commands(['6', '+ 5', '+ 2', '+ 3', '-', '-', '+ 7', '-'], 6), '3\n2\n7')

if __name__ == '__main__':
    unittest.main()