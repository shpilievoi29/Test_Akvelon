import unittest
from numberTranslator import NumberFormatter


class MyTestCase(unittest.TestCase):
    def test_string(self):
        self.assertEqual(NumberFormatter("10").parseInt(), 10)

    def test_empty(self):
        self.assertEqual(NumberFormatter("").parseInt(), "you entered wrong format")

    def test_not_string(self):
        self.assertEqual(NumberFormatter(15).parseInt(), "you entered wrong format")

    def test_negative_number(self):
        self.assertEqual(NumberFormatter("-10234234").parseInt(), -10234234)

    def test_positive_number(self):
        self.assertEqual(NumberFormatter("+10").parseInt(), 10)

    def test_float(self):
        self.assertEqual(NumberFormatter(10.1).parseInt(), "you entered wrong format")


if __name__ == '__main__':
    unittest.main()
