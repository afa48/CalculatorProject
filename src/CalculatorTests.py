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
        test_data.clear()

    def test_subtract_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Subtraction.csv').data
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        test_data.clear()

    def test_multiply_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Multiplication.csv').data
        print("multiply ")
        pprint(test_data)
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
        test_data.clear()

    def test_divide(self):
        test_data = CsvReader('/src/Unit Test Division.csv').data
        pprint (test_data)
        for row in test_data:
            self.assertEqual(self.calculator.divide(float(row['Value 1']), float(row['Value 2'])), float(row['Result']))
        test_data.clear()

    def test_squared_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.squared(row['Value 1']), row['Result'])
            self.assertEqual(self.calculator.result, row['Result'])
        test_data.clear()

    def test_squareRooted_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Square Root.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.squarerooted(float(row['Value 1'])), "{:.9}".format(float(row['Result'])))
        test_data.clear()

if __name__ == '__main__':
    unittest.main()
