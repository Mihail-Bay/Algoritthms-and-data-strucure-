import unittest
from Lab7.task7.src.templates import template

class TestTemplateMatching(unittest.TestCase):

    def test_exact_match(self):
        self.assertEqual(template("abc", "abc"), "YES")

    def test_question_mark_match(self):
        self.assertEqual(template("a?c", "abc"), "YES")
        self.assertEqual(template("a?c", "acc"), "YES")
        self.assertEqual(template("a?c", "abx"), "NO")

    def test_asterisk_match(self):
        self.assertEqual(template("*", "abc"), "YES")
        self.assertEqual(template("a*", "abc"), "YES")
        self.assertEqual(template("*c", "abc"), "YES")
        self.assertEqual(template("a*b", "aabb"), "YES")
        self.assertEqual(template("a*b", "ab"), "YES")
        self.assertEqual(template("a*b", "b"), "NO")

    def test_multiple_asterisks(self):
        self.assertEqual(template("*a*b*", "xxaabbxx"), "YES")
        self.assertEqual(template("*a*b*c*", "xxaabbccxx"), "YES")
        self.assertEqual(template("*a*b*c*", "xxaaxbbxx"), "NO")

    def test_no_match(self):
        self.assertEqual(template("abc", "def"), "NO")
        self.assertEqual(template("a?c", "abcx"), "NO")
        self.assertEqual(template("a*b", "xyz"), "NO")

    def test_empty_string_and_pattern(self):
        self.assertEqual(template("", ""), "YES")
        self.assertEqual(template("a", ""), "NO")
        self.assertEqual(template("", "a"), "NO")
        self.assertEqual(template("*", ""), "YES")
        self.assertEqual(template("a*", ""), "NO")

if __name__ == '__main__':
    unittest.main()