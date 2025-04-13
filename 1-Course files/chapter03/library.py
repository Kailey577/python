import math

def NextGuess(guess, x: float)->float:
    return (guess/2 + x/(guess/2))/2
'''finds square root of x'''
#assert NextGuess(20,25)==5
#assert NextGuess(30,100)==10

x = float(input("Type value of number you want square root of: "))
guess = int(input("How many times do you want to guess?: "))
def NextGuess(how,x):
    first_guess = x/2

    for i in range(how):
        first_guess = (first_guess + x/first_guess)/2

    print(first_guess)
    print(math.sqrt(x)-first_guess)

NextGuess(guess,x)
