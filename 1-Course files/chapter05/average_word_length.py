user_input = input("Please enter your sentence: ")

words = len(user_input.split(" "))
print(words)
characters = len(user_input.replace(" ",""))
print(characters)


average = characters/words

print(average)

