

user_input = input("Please type in a phrase!!: ").split(" ")

amount = len(user_input)
print(user_input)
print(amount)

total = []
for i in range(amount):
    total.append(user_input[i][0].upper())

print(" ".join(total))