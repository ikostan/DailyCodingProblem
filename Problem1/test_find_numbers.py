import unittest
from Problem_1 import find_numbers


class TestFindNumbers(unittest.TestCase):
    def test_basic(self):
        # given [10, 15, 3, 7] and k of 17, return [10, 7] since 10 + 7 is 17.
        goal = 17
        numbers = [10, 15, 3, 7]
        answer = [10, 7]
        self.assertListEqual(answer, find_numbers(goal, numbers))

    def test_false_case(self):
        # given [10, 15, 3, 9] and k of 17, return False.
        goal = 17
        numbers = [10, 15, 3, 9]
        self.assertFalse(find_numbers(goal, numbers))

    def test_negative_number(self):
        # given [10, 15, 3, 7] and k of 17, return [10, -15] since 10 + (-15) is -5.
        goal = -5
        numbers = [10, -15, 3, 7]
        answer = [10, -15]
        self.assertListEqual(answer, find_numbers(goal, numbers))

    def test_zero(self):
        # given [10, 15, 3, 7] and k of 17, return [-15, 15] since 15 + (-15) is 0.
        goal = 0
        numbers = [10, -15, 3, 7, 15]
        answer = [-15, 15]
        self.assertListEqual(answer, find_numbers(goal, numbers))

    def test_not_null(self):
        # given [10, 15, 3, 7] and k of 17, return [-15, 15] since 15 + (-15) is 0.
        goal = 0
        numbers = [10, -15, 3, 7, 15]
        answer = [-15, 15]
        self.assertIsNotNone(find_numbers(goal, numbers))