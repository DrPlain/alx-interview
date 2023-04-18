import unittest
pascal_triangle = __import__('0-pascal_triangle').pascal_triangle


class TestPascalTriangle(unittest.TestCase):
    def test_n_less_or_equal_to_zero(self):
        n = -4
        n2 = 0
        self.assertEqual(pascal_triangle(n), [])
        self.assertEqual(pascal_triangle(n2), [])

    def test_n_equals_one(self):
        n = 1
        self.assertEqual(pascal_triangle(n), [[1]])

    def test_n_equals_two(self):
        n = 2
        self.assertEqual(pascal_triangle(n), [[1], [1, 1]])

    def test_n_equals_four(self):
        n = 4
        self.assertEqual(pascal_triangle(
            4), [[1], [1, 1], [1, 2, 1], [1, 3, 3, 1]])
