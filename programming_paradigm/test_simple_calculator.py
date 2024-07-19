# simple_calculator.py
class SimpleCalculator:
    """A simple calculator class that supports basic arithmetic operations."""

    def add(self, a, b):
        """Return the addition of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the subtraction of b from a."""
        return a - b

    def multiply(self, a, b):
        """Return the multiplication of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the division of a by b. Returns None if b is zero."""
        if b == 0:
            return None
        return a / b
import unittest
from Simple_Calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        self.calculator = SimpleCalculator()

    def test_add(self):
        result = self.calculator.add(3, 5)
        self.assertEqual(result, 8)

    def test_subtract(self):
        result = self.calculator.subtract(10, 4)
        self.assertEqual(result, 6)

    def test_multiply(self):
        result = self.calculator.multiply(2, 5)
        self.assertEqual(result, 10)

    def test_divide(self):
        result = self.calculator.divide(8, 2)
        self.assertEqual(result, 4)

        result = self.calculator.divide(5, 0)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()

