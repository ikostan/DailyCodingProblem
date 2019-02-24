import unittest
from Problem4 import find_first_missing_positive_integer

class TestProblem4(unittest.TestCase):
    def test_output_is_not_null(self):
        input_list = [3, 4, -1, 1]
        self.assertIsNotNone(find_first_missing_positive_integer(input_list))

    def test_basic_1(self):
        # The input [3, 4, -1, 1] should give 2.
        input_array = [3, 4, -1, 1]
        expected = 2
        self.assertEqual(expected, find_first_missing_positive_integer(input_array))

    def test_basic_2(self):
        # The input [1, 2, 0] should give 3
        input_array = [1, 2, 0]
        expected = 3
        self.assertEqual(expected, find_first_missing_positive_integer(input_array))
