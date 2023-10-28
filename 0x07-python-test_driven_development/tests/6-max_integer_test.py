#!/usr/bin/python3
"""unittest for max_integer([...])"""

import unittest
"""unittest for max_integer([...])"""
max_integer = __import__('6-max_integer').max_integer
"""Function to find and return the max integer in a list of integers"""


class TestMaxInteger(unittest.TestCase):
    """unittest for max_integer([...])"""

    def test_max_integer(self):
        self.assertEqual(max_integer([1, 2, 3, 4]), 4)
        self.assertEqual(max_integer([1, 3, 4, 2, 5]), 5)
        self.assertEqual(max_integer([1, 2, 3]), 3)

    def test_max_integer_with_empty_list(self):
        self.assertIsNone(max_integer([]))

    def test_max_integer_with_one_element(self):
        self.assertEqual(max_integer([1]), 1)

    def test_max_negative_numbers(self):
        self.assertEqual(max_integer([-1, -2, -3]), -1)


if __name__ == "__main__":
    unittest.main()
