def sum_cube_n(n: int)->int:
    "returns sum of first cubed n numbers"
    #sum = (((n * n * (n + 1) ** 2) / 4))
    #return sum
    cube_sum = 0
    for i in range(n + 1):
        cube_sum = i ** 3 + cube_sum
    return cube_sum

assert sum_cube_n(3) == 1**3 + 2**3 + 3**3
assert sum_cube_n(10) == ((10 * 10 * (10 + 1) ** 2) / 4)



#....

print(sum_cube_n(10))