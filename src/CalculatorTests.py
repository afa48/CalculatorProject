import unittest
from Calculator import Calculator


class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        self.assertEqual(self.calculator.add(2, -2), 0)
        self.assertEqual(self.calculator.result, 0)

    def test_subtract_method_calculator(self):
        self.assertEqual(self.calculator.subtract(4, 2), 2)
        self.assertEqual(self.calculator.result, 2)

    def test_multiply_method_calculator(self):
        self.assertEqual(self.calculator.multiply(2, 2), 4)
        self.assertEqual(self.calculator.result, 4)

    def test_divide_method_calculator(self):
        self.assertEqual(self.calculator.divide(12, 2), 6)
        self.assertEqual(self.calculator.result, 6)

    def test_squared_method_calculator(self):
        self.assertEqual(self.calculator.squared(3), 9)
        self.assertEqual(self.calculator.result, 9)

    def test_squareRooted_method_calculator(self):
        self.assertEqual(self.calculator.squareRooted(25), 5)
        self.assertEqual(self.calculator.result, 5)

if __name__ == '__main__':
    unittest.main()
