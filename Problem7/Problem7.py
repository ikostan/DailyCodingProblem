'''

This problem was asked by Facebook.

Given the mapping a = 1, b = 2, ... z = 26, and an encoded message,
count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa',
'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.

'''

import string


def decoder(msg):
    alphabet = list(string.ascii_lowercase)
    codes = dict(enumerate(alphabet, 1))
    possible_messages = set()
    size = len(msg)



    return possible_messages

