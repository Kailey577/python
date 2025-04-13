
'''12. Write and test a function to meet this specification.
sumList(nums) nums is a list of numbers. Retur
ns the sum of the numbers in the list.'''

def sumList(nums):
    print(nums)
    hey = sum(list(map(int, nums)))
    print(hey)


nums = list(input("create list of numbers: "))
sumList(nums)