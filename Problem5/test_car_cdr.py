import unittest
import Problem5


class TestCarCdr(unittest.TestCase):

    # car(cons(3, 4)) returns 3.
    def test_car(self):
        a = 3
        b = 4
        self.assertEqual(a, Problem5.car(Problem5.cons(a, b)))

    # cdr(cons(3, 4)) returns 4.
    def test_cdr(self):
        a = 3
        b = 4
        self.assertEqual(b, Problem5.cdr(Problem5.cons(a, b)))

