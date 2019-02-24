'''
This problem was asked by Uber.

Given an array of integers, return a new array such that each element
at index i of the new array is the product of all the numbers in the
original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output
would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1],
the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?
'''

def generate_array(input_array):
    output_array = list()

    for n in input_array:
        i = input_array.index(n)
        result = multiply_list_members(input_array, i)
        print("For " + str(n) + " result number is " + str(result))
        output_array.append(result)

    print()

    return output_array


def multiply_list_members(input_array, i):
    result = 1

    for n in range(len(input_array)):
        if n != i:
            result *= input_array[n]

    return result
