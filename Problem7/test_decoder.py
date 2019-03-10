import unittest
from Problem7 import decoder


class TestDecoder(unittest.TestCase):

    def test_output(self):
        message = '111'
        result = ('aaa', 'ka', 'ak')
        self.assertListEqual(list(decoder(message)), list(result))

    def test_output_len(self):
        message = '111'
        result = ('aaa', 'ka', 'ak')
        n = len(result)
        self.assertEqual(len(decoder(message)), n)


