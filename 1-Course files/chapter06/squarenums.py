'''11. Write and test a function to meet this specification.
squareEach(nums) nums is a list of numbers. Modifies the list by squaring each entry.
'''
import math
def square_num_list(nums:list)->list:
    #squares all numbers in list
    return [nums**2]


    assert square_num_list([1,2,3]) == [1**2,2**2,3**2]
    assert square_num_list([2,1,11]) == [2**2,1**2,11**2]

# list(int) -> list(int)
def square_num_list(nums:[int]) -> [int]:
    new_list = []
    for number in nums:
        square = number * number
        new_list.append(square)
    return new_list













