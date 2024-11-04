import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)

    # Add the following test methods to the TestCalculator class:

    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_add_zero(self):
        self.assertEqual(self.calc.add(1, 0), 1)

    def test_sub_01(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
    
    def test_sub_02(self):
        self.assertEqual(self.calc.subtract(1, 1), 0)

    def test_multiply_01(self):
        self.assertEqual(self.calc.multiply(2, 1), 2)

    def test_multiply_02(self):
        self.assertEqual(self.calc.multiply(2, 0), 0)

    def test_divide_01(self):
        self.assertEqual(self.calc.divide(4, 2), 2)

    def test_divide_02(self):
        self.assertEqual(self.calc.divide(2, 2), 1)

    def test_modulo_01(self):
        self.assertEqual(self.calc.modulo(2, 2), 0)

    def test_modulo_02(self):
        self.assertEqual(self.calc.modulo(4, 3), 1)

if __name__ == '__main__':
    unittest.main()