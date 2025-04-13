import math
def main():
    user_input = int(input("Enter a positive whole number above 2: "))
    while user_input <= 2:
        user_input = int(input("Enter a positive whole number above 2: "))
    #user_input//user_input -> 2
    starting_number = 2
    while user_input%starting_number != 0:
        if starting_number <= math.sqrt(user_input):
            print(math.sqrt(user_input))
            a_variable = user_input / starting_number
            print(a_variable)
            starting_number = starting_number + 1
        else:
            print("This number is prime")
            quit()

    print("This number is divisible by", starting_number)
main()