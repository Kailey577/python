
def main():
    user_input = int(input("Enter an even number: "))
    while user_input//2 != 0:
        user_input = int(input("Enter an even number: "))

    value_1 = user_input/2
    value_2 = user_input/2

    while value_1 < user_input and value_2 < user_input:

