import unittest
from fractions_doctest import sum_fractions, mult_fractions


class TestFractions(unittest.TestCase):
    def test_sum_fractions(self):
        self.assertEqual(sum_fractions(3, 4, 7, 8), '13/8')

    def test_mult_fractions(self):
        self.assertEqual(mult_fractions(3, 4, 7, 8), '21/32')


if __name__ == '__main__':
    unittest.main(verbosity=True)
