# File: chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))

    k = eval(input("Enter a number between 0 and 1: "))

    for i in range(10):
        k = 3.9 * k * (1 - x)
        x = 3.9 * x * (1 - x)
        print(str(k)+" "+str(x))



main()