'''
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''

def find_numbers(goal, numbers):

    for n in numbers:
        n2 = goal - n
        if n2 in numbers:
            nums = [n, n2]
            return nums

    return False

