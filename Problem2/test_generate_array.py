import unittest
from Problem2 import generate_array

class TestGenerateArray(unittest.TestCase):
    # verify that method does not return null
    def test_not_null(self):
        self.assertIsNotNone(generate_array(list()))

    # if our input was [1, 2, 3, 4, 5], the expected output
    # would be [120, 60, 40, 30, 24].
    def test_basic_case_1(self):
        input_array = [1, 2, 3, 4, 5]
        output_array = [120, 60, 40, 30, 24]
        self.assertListEqual(generate_array(input_array), output_array)

    # If our input was [3, 2, 1],
    # the expected output would be [2, 3, 6].
    def test_basic_case_2(self):
        input_array = [3, 2, 1]
        output_array = [2, 3, 6]
        self.assertListEqual(generate_array(input_array), output_array)


