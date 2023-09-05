"""Unit tests of the Statistics class."""
from unittest import TestCase
from statistics import average, variance


class StatisticsTest(TestCase):

    # Example of a descriptive test name and descriptive docstring

    def test_variance_empty_list_throws_exception(self):
        """variance of an empty list must raise an exception"""
        with self.assertRaises(ValueError):
            variance([])

    def test_variance_all_numbers_are_zero(self):
        """If a list is contained only zero, the variance must be zero"""
        self.assertEqual(variance([0]), 0)
        self.assertEqual(variance([0] * 100), 0)

    def test_avg_empty_list_throws_exception(self):
        """average of an empty list must raise an exception"""
        with self.assertRaises(ValueError):
            average([])

    def test_avg_all_numbers_are_zero(self):
        """If a list is contained only zero, the average must be zero"""
        self.assertEqual(average([0]), 0)
        self.assertEqual(average([0] * 100), 0)


if __name__ == '__main__':
    # another way to run unit test
    import unittest
    unittest.main(verbosity=1)

