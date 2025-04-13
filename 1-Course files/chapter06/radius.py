from math import pi

def area_of_sphere(radius:float)->float:
    """
    returns area of sphere with radius
    """
    return 4*pi*radius*radius

assert area_of_sphere(3.0) == 4*pi*3.0*3.0
assert area_of_sphere(4.0) == 4*pi*4.0*4.0

def sum_n(n:int)->int:
    '''
    returns sum of first n numbers
    '''
    the_sum = 0
    for i in range(n+1):
        the_sum = the_sum + i
    return the_sum

assert sum_n(3) == 1 + 2 + 3
assert sum_n(10) == (10*11)/2

# [float] -> int/float
def sum_list(numbers:[float]) -> float:
    """
    writes tuff later
    """

#assert sum_list([1,2,3) == 1 + 2 + 3


def foo() -> None:
    print(x)



foo()
x = 10



