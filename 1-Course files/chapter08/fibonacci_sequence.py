from setuptools.sandbox import save_argv


def fibonacci(num: int)->int:
    a = 0
    b = 1
    assert fibonacci(3) == 2
    assert fibonacci(1) == 1

    if num == 2 or num == 1:
        return b
    elif num == 0:
        return a
    else:
        for i in range(1,num):
            c = a + b
            a = b
            b = c
        return b



user_input = int(input("Enter the number: "))
print(fibonacci(user_input))