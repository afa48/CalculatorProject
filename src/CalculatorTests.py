import unittest
from Calculator import Calculator
from CsvReader import CsvReader

from pprint import pprint

class MyTestCase(unittest.TestCase):

    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_result_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Addition.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

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
        self.assertEqual(self.calculator.squarerooted(25), 5)
        self.assertEqual(self.calculator.result, 5)

if __name__ == '__main__':
    unittest.main()
