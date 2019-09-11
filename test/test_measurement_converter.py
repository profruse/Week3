import unittest
from main_source import measurement_converter
import unittest.mock as mock


class MyTestCase(unittest.TestCase):

    def test_twelve_inches(self):
        self.assertEqual(1, measurement_converter.convert_inches_to_feet(12))

    def test_twenty_four_inches(self):
        self.assertEqual(2, measurement_converter.convert_inches_to_feet(24))

    def test_ten_inches(self):
        self.assertEqual(0, measurement_converter.convert_inches_to_feet(10))

    def test_twenty_eight_inches(self):
        self.assertEqual(2, measurement_converter.convert_inches_to_feet(28))

    def test_negative_twelve_inches(self):
        self.assertEqual(0, measurement_converter.convert_inches_to_feet(-12))

    def test_zero_inches(self):
        self.assertEqual(0, measurement_converter.convert_inches_to_feet(0))
    def test_one_plus_one(self):
        with mock.patch('builtins.input',side_effect=[1,1]):
            assert measurement_converter.addition() == 2


if __name__ == '__main__':
    unittest.main()
