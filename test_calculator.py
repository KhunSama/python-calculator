import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(2, 1), 3)
    
    # Add the following test methods to the TestCalculator class:
    def test_add_negative(self):
        self.assertEqual(self.calc.add(-1, 2), 1)
        self.assertEqual(self.calc.add(1, -2), -1)
        self.assertEqual(self.calc.add(-1, -2), -3)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(2, 1), 1)
        self.assertEqual(self.calc.subtract(1, 2), -1)
    def test_subtract_negative(self):
        self.assertEqual(self.calc.subtract(2, -1), 3)
        self.assertEqual(self.calc.subtract(-2, 1), -3)
        self.assertEqual(self.calc.subtract(-2, -1), -1)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(4, 5), 20)
        self.assertEqual(self.calc.multiply(5, 4), 20)
    def test_multiply_negative(self):
        self.assertEqual(self.calc.multiply(-1, 2), -2)
        self.assertEqual(self.calc.multiply(1, -2), -2)
        self.assertEqual(self.calc.multiply(-1, -2), 2)
        self.assertEqual(self.calc.multiply(-5, -2), 10)
        self.assertEqual(self.calc.multiply(-9, -9), 81)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(5, 10), 0)
        self.assertEqual(self.calc.divide(1000, 5), 200)
    def test_divide_negative(self):
        self.assertEqual(self.calc.divide(-10, 5), -2)
        self.assertEqual(self.calc.divide(5, -10), 0)
        # self.assertEqual(self.calc.divide(-10, -5), 2)




if __name__ == '__main__':
    unittest.main()