# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future

def main():
    print("This program calculates the future value")
    print("of an investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    year = eval(input("Enter how many years:"))

    for i in range(10):
        principal = principal * (1 + apr)

    print("The value in " + str(year) + " year(s) is:", principal)

main()
