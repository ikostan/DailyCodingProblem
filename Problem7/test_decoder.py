import unittest
from Problem7 import decoder


class TestDecoder(unittest.TestCase):

    def test_basic_output(self):
        message = '111'
        result = ('aaa', 'ka', 'ak')
        self.assertListEqual(sorted(list(decoder(message))), sorted(list(result)))

    def test_basic_output_len(self):
        message = '111'
        result = ('aaa', 'ka', 'ak')
        n = len(result)
        self.assertEqual(len(decoder(message)), n)

    # Following test cases were taken from https://galaiko.rocks/posts/2018-07-08/ :
    # 2 ways to decode: 1,3 / 13
    def test_13(self):
        message = '13'
        n = 2
        self.assertEqual(len(decoder(message)), n)

    # 113: 3  ways
    # 1, 1, 3 / 11, 3 / 1, 13
    def test_113(self):
        message = '113'
        n = 3
        self.assertEqual(len(decoder(message)), n)

    # 1113: 5 ways
    # 1, 1, 1, 3 / 11, 1, 3 / 11, 13 / 1, 11, 3 / 1, 1, 13
    def test_1113(self):
        message = '1113'
        n = 5
        self.assertEqual(len(decoder(message)), n)

    # 11113: 8 ways
    # 1, 1, 1, 1, 3 / 11, 1, 1, 3 / 11, 11, 3 / 11, 1, 13 / 1, 11, 1, 3 / 1, 11, 13 /
    # 1, 1, 11, 3 / 1, 1, 1, 13
    def test_11113(self):
        message = '11113'
        n = 8
        self.assertEqual(len(decoder(message)), n)

    # 27: 1 ways
    # 2, 7
    def test_27(self):
        message = '27'
        n = 1
        self.assertEqual(len(decoder(message)), n)

    # 227: 2 ways
    # 2, 2, 7 / 22, 7
    def test_227(self):
        message = '227'
        n = 2
        self.assertEqual(len(decoder(message)), n)

    # 2227: 3 ways
    # 2, 2, 2, 7 / 22, 2, 7 / 2, 22, 7
    def test_2227(self):
        message = '2227'
        n = 3
        self.assertEqual(len(decoder(message)), n)

    # 22227: 5 ways
    # 2, 2, 2, 2, 7 / 22, 2, 2, 7 / 22, 22, 7 / 2, 22, 2, 7 / 2, 2, 22, 7
    def test_22227(self):
        message = '22227'
        n = 5
        self.assertEqual(len(decoder(message)), n)

    # 222227: 8 ways
    # 2, 2, 2, 2, 2, 7 / 22, 2, 2, 2, 7 / 22, 22, 2, 7 / 22, 2, 22, 7 / 2, 22, 2, 2, 7 / 2, 22, 22, 7 /
    # 2, 2, 22, 2, 7 / 2, 2, 2, 22, 7
    def test_222227(self):
        message = '222227'
        n = 8
        self.assertEqual(len(decoder(message)), n)

    # 2222227: 13 ways
    # 2, 2, 2, 2, 2, 2, 7 / 22, 2, 2, 2, 2, 7 / 22, 22, 2, 2, 7 / 22, 22, 22, 7 / 22, 2, 22, 2, 7 / 22, 2, 2, 22, 7 /
    # 2, 22, 2, 2, 2, 7 / 2, 22, 22, 2, 7 / 2, 22, 2, 22, 7 / 2, 2, 22, 2, 2, 7 / 2, 2, 22, 22, 7 / 2, 2, 2, 22, 2, 7 /
    # 2, 2, 2, 2, 22, 7
    def test_2222227(self):
        message = '2222227'
        n = 13
        self.assertEqual(len(decoder(message)), n)


