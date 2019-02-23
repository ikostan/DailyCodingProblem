import unittest
from Problem_1 import find_numbers

class TestFindNumbers(unittest.TestCase):
    def test_basic(self):
        # given [10, 15, 3, 7] and k of 17, return [10, 7] since 10 + 7 is 17.
        goal = 17
        numbers = [10, 15, 3, 7]
        answer = [10, 7]
        self.assertListEqual(answer, find_numbers(goal, numbers))

    def test_false(self):
        # given [10, 15, 3, 9] and k of 17, return False.
        goal = 17
        numbers = [10, 15, 3, 9]
        self.assertFalse(find_numbers(goal, numbers))