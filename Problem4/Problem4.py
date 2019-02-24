'''
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer
in linear time and constant space. In other words, find the lowest
positive integer that does not exist in the array. The array can contain
duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

def find_first_missing_positive_integer(input_list):
    number = None
    numbers_list = list()

    # Sort the list:
    input_list.sort()
    #print(input_list)

    # Find is there any missing int between two array members
    for n in range(len(input_list) - 1):
        num = input_list[n+1] - input_list[n]
        if num > 1:
            numbers_list.append(num)

    # Test is there any valid missing integers, if not create a new one
    if len(numbers_list) > 0:
        number = min(numbers_list)
    else:
        number = max(input_list) + 1

    return number

