from unittest import TestCase

from Problem_1 import find_numbers

class Test_find_numbers(TestCase):
    def test_find_numbers(self):
        goal = 17
        numbers = [10, 15, 3, 7]
        goal_numbers = [10, 7]
        self.assertEqual(find_numbers(goal, numbers), goal_numbers)

    def false_test_find_numbers(self):
        goal = 7
        numbers = [3, 2, 6, 8]
        self.assertFalse(find_numbers(goal, numbers))








