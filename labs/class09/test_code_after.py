import unittest

from labs.class09.code_before import SumDigits

class TestSumDigits(unittest.TestCase):
    def setUp(self):
        self.sum_digits = SumDigits()
    
    def test_single_digit_positive(self):
        self.assertEqual(self.sum_digits.sum_digits(5), 5)
    
    def test_multi_digit_positive(self):
        self.assertEqual(self.sum_digits.sum_digits(123), 6)
    
    def test_zero(self):
        self.assertEqual(self.sum_digits.sum_digits(0), 0)
    
    def test_negative_number(self):
        self.assertEqual(self.sum_digits.sum_digits(-123), 6)
    
    def test_large_number(self):
        self.assertEqual(self.sum_digits.sum_digits(9999), 36)
    
    def test_number_with_zeros(self):
        self.assertEqual(self.sum_digits.sum_digits(1001), 2)


if __name__ == '__main__':
    unittest.main()