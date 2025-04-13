
user_input = int(input("ENTER YOUR AMOUNT OF POINTS: "))

if user_input < 0:
    print("NOT VALID")
    quit()
if user_input > 5:
    print("NOT VALID")
    quit()
if user_input <= 1:
    print("F")
if user_input == 5:
    print("A")
if user_input == 4:
    print("B")
if user_input == 3:
    print("C")
if user_input == 2:
    print("D")