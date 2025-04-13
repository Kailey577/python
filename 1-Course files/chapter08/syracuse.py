def main():
    user_input = int(input("ENTER A NUMBER: "))
    print(user_input)
    if user_input%2 == 0:
        while user_input > 1:
            user_input = user_input/2
            print(user_input)
    else:
        user_input = 3*user_input + 1
        print(user_input)
        while user_input > 1:
            user_input = user_input/2
            print(user_input)


main()