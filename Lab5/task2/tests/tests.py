import unittest
from Lab5.task2.src.tree_height import TreeHeightCalculator

class TestTreeHeightCalculator(unittest.TestCase):

    def setUp(self):
        # Подготовка тестовых данных
        self.calculator = TreeHeightCalculator()

    def test_tree_height_single_node(self):
        # Тест для дерева с одним узлом
        self.calculator.n = 1
        self.calculator.parents = [-1]
        expected_height = 1
        result = self.calculator.tree_height(self.calculator.n, self.calculator.parents)
        self.assertEqual(result, expected_height)

    def test_tree_height_two_nodes(self):
        # Тест для дерева с двумя узлами
        self.calculator.n = 2
        self.calculator.parents = [-1, 0]  # Узел 0 - корень, узел 1 - дочерний
        expected_height = 2
        result = self.calculator.tree_height(self.calculator.n, self.calculator.parents)
        self.assertEqual(result, expected_height)

    def test_tree_height_complex_tree(self):
        # Тест для более сложного дерева
        self.calculator.n = 5
        self.calculator.parents = [-1, 0, 0, 1, 1]  # Корень 0, узлы 1 и 2 - дочерние к 0, 3 и 4 - дочерние к 1
        expected_height = 3
        result = self.calculator.tree_height(self.calculator.n, self.calculator.parents)
        self.assertEqual(result, expected_height)


if __name__ == '__main__':
    unittest.main()