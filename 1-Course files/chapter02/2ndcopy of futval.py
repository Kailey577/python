# futval.py
#    A program to compute the value of an investment
#    carried 10 years into the future
'''

'''
def main():
    print("This program calculates the future value")
    print("of a 10-year investment.")

    principal = eval(input("Enter the initial principal: "))
    apr = eval(input("Enter the annual interest rate: "))
    period = eval(input("Enter the number of periods per year:"))

    for i in range(10*period):
        principal = principal * (1 + apr/period)

    print("The value in 10 years is:", principal)

main()
