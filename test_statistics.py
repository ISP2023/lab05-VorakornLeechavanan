"""Unit tests of the Statistics class."""
from unittest import TestCase
from statistics import average, variance


class StatisticsTest(TestCase):

    # Example of a descriptive test name and descriptive docstring

    def test_variance_empty_list_throws_exception(self):
        """variance of an empty list should raise an exception"""
        pass


if __name__ == '__main__':
    # another way to run unit test
    import unittest
    unittest.main(verbosity=1)

