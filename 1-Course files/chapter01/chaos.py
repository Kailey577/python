# File: chaos.py
# A simple program illustrating chaotic behavior.

def main():
    print("This program illustrates a chaotic function")
    x = eval(input("Enter a number between 0 and 1: "))
    b = eval(input("Enter how many rows u want:"))
    for i in range(b):

        x = 3.9 * x * (1 - x)
        print(x)

main()