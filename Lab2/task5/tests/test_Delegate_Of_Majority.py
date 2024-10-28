import unittest
from Lab2.task5.src.Delegate_Of_Majority import *


class TestMajorityElement(unittest.TestCase):

    def test_majority_element_exist(self):
        self.assertEqual(majority_element([3, 3, 4, 2, 4, 4, 2, 4]), 0)  # 4 является элементом большинства
        self.assertEqual(majority_element([1, 1, 2, 1, 2, 1]), 1)      # 1 является элементом большинства

    def test_majority_element_not_exist(self):
        self.assertEqual(majority_element([1, 2, 3, 4]), 0)           # Нет элемента большинства
        self.assertEqual(majority_element([1, 2, 2, 3, 3]), 0)        # Также нет элемента большинства

    def test_single_element_list(self):
        self.assertEqual(majority_element([1]), 1)                    # Единственный элемент считается элементом большинства

    def test_multiple_same_elements(self):
        self.assertEqual(majority_element([2, 2, 2, 2, 2]), 1)        # Все элементы одинаковы

if __name__ == '__main__':
    unittest.main()