import unittest
from Calculator import Calculator
from CsvReader import CsvReader


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
            test_data.clear(CsvReader('/src/Unit Test Addition.csv'))

    def test_subtract_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Subtraction.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
            test_data.clear(CsvReader('/src/Unit Test Subtraction.csv'))

    def test_multiply_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Multiplication.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.multiply(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
            test_data.clear(CsvReader('/src/Unit Test Multiplication.csv'))

    def test_divide_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Division.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.divide(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
            test_data.clear(CsvReader('/src/Unit Test Division.csv'))

    def test_squared_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Square.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.squared(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
            test_data.clear(CsvReader('/src/Unit Test Square.csv'))

    def test_squareRooted_method_calculator(self):
        test_data = CsvReader('/src/Unit Test Square Root.csv').data
        for row in test_data:
            self.assertEqual(self.calculator.squarerooted(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))
            test_data.clear(CsvReader('/src/Unit Test Square Root.csv'))

if __name__ == '__main__':
    unittest.main()
