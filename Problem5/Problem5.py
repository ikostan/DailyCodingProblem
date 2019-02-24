'''

This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair)
returns the first and last element of that pair. For example,
car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:

def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair

Implement car and cdr.

'''


# constructs a pair
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair


# returns the first element of that pair
def car(f):
    def first(a, b):
        return a
    return f(first)


# returns the last element of that pair
def cdr(f):
    def last(a, b):
        return b
    return f(last)

