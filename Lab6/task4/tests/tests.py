import unittest
from Lab6.task1.src.Array import *

class TestCustomSet(unittest.TestCase):

    def setUp(self):
        """Создание нового экземпляра CustomSet перед каждым тестом."""
        self.custom_set = CustomSet()

    def test_should_add_element(self):
        """Тестирование добавления элементов в множество."""
        self.custom_set.add(5)
        self.assertTrue(self.custom_set.exists(5), "Element 5 should exist after adding.")

        self.custom_set.add(10)
        self.assertTrue(self.custom_set.exists(10), "Element 10 should exist after adding.")

    def test_should_remove_element(self):
        """Тестирование удаления элементов из множества."""
        self.custom_set.add(5)
        self.custom_set.remove(5)
        self.assertFalse(self.custom_set.exists(5), "Element 5 should not exist after removing.")

    def test_should_exists_element(self):
        """Тестирование проверки существования элементов в множестве."""
        self.custom_set.add(25)
        self.assertTrue(self.custom_set.exists(25), "Element 25 should exist after adding.")

        self.assertFalse(self.custom_set.exists(30), "Element 30 should not exist if not added.")


if __name__ == '__main__':
    unittest.main()