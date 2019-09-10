import unittest
from main_source import measurement_converter


class MyTestCase(unittest.TestCase):
    def test_twenty_eight_inches(self):
        self.assertEqual(2, measurement_converter.convert_inches_to_feet(28))

    def test_twelve_inches(self):
        self.assertEqual(1, measurement_converter.convert_inches_to_feet(12))

    def test_twenty_four_inches(self):
        self.assertEqual(2, measurement_converter.convert_inches_to_feet(24))

    def test_ten_inches(self):
        self.assertEqual(0, measurement_converter.convert_inches_to_feet(10))


if __name__ == '__main__':
    unittest.main()
