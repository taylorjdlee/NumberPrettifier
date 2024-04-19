import unittest
from prettifier import number_prettifier

class TestPrettifier(unittest.TestCase):
    def test_negative_number(self):
        self.assertEqual(number_prettifier(-1000000), "Negative number cannot be prettified")

    def test_millions(self):
        self.assertEqual(number_prettifier(1000000), "1M")

    def test_millions_decimal(self):
        self.assertEqual(number_prettifier(2500000.34), "2.5M")

    def test_small_number(self):
        self.assertEqual(number_prettifier(532), "532")

    def test_thousands(self):
        self.assertEqual(number_prettifier(999999), "999999")

    def test_billion(self):
        self.assertEqual(number_prettifier(1123456789), "1.1B")

    def test_billions(self):
        self.assertEqual(number_prettifier(46123456789), "46.1B")
    
    def test_trillions(self):
        self.assertEqual(number_prettifier(2363328525568), "2.4T")

    def test_trillions_2(self):
        self.assertEqual(number_prettifier(67763328525568), "67.8T")
    
    def test_quadrillions(self):
        self.assertEqual(number_prettifier(2000000000000000), "Number too large to prettify")

if __name__ == '__main__':
    unittest.main()
