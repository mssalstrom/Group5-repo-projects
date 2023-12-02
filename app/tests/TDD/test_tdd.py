from even_checker import is_even
from my_calculator import add_numbers
import unittest


class TestEvenChecker(unittest.TestCase):
    def test_is_even(self):
        self.assertTrue(is_even(4))
        self.assertFalse(is_even(7))


class TestCalculator(unittest.TestCase):
    def test_add_numbers(self):
        result = add_numbers(2, 3)
        self.assertEqual(result, 5)


if __name__ == '__main__':
    unittest.main()
