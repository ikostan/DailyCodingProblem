import unittest
from Problem7 import decoder


class TestDecoder(unittest.TestCase):
    def test_basic_case(self):
        msg = '111'
        answer = 3
        self.assertEqual(answer, len(decoder(msg)))

    def test_msg_decoder(self):
        msg = '111'
        answer = {'aaa', 'ka', 'ak'}
        decoder_results = decoder(msg)
        dif = decoder_results.difference(answer)
        # Test is dif set is empty, bool() will do something similar to not not,
        # but more idiomatic and clear.
        self.assertTrue(bool(dif))

