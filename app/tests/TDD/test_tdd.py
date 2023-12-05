# Importing the 'is_even' function from the 'even_checker' module
from even_checker import is_even
# Importing the necessary module or function from 'my_calculator'
from my_calculator import add_numbers
# Importing the 'unittest' module for creating test cases
import unittest


# Creating a test class that inherits from 'unittest.TestCase'
class TestEvenChecker(unittest.TestCase):
    # Defining a test method for the 'is_even' function
    def test_is_even(self):
        # Asserting that is_even(4) returns True (since 4 is an even number)
        self.assertTrue(is_even(4))
        # Asserting that is_even(7) returns False (since 7 is an odd number)
        self.assertFalse(is_even(7))


# This script can be executed to run the test defined in the 'TestCalculator' class
# Example usage:
# if __name__ == '__main__':
#     unittest.main()


# Creating a test class that inherits from 'unittest.TestCase'
class TestCalculator(unittest.TestCase):
    # Defining a test method for the 'add_numbers' function
    def test_add_numbers(self):
        # Calling the 'add_numbers' function with arguments 2 and 3
        result = add_numbers(2, 3)
        # Asserting that the result is equal to the expected value (5)
        self.assertEqual(result, 5)


