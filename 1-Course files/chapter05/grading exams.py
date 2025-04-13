user_input = (input("ENTER YOUR EXAM SCORE: "))

grade_letters = ["A","B","C","D","F"]

first_digit = int(user_input[0])

print(first_digit)
#10 - 1 = 9
#10 - 9 = 1
#10 - 8 = 2
a = 10 - first_digit -1
print(grade_letters[a])
#first_digit - (first_digit-0)
#first_digit - (first_digit - 1)
#first_digit - (first_digit - 2)
#1-1 = 0, 9 - 8 = 1, 8 - 6 = 2, 7 - 4 = 3

# 1 is 0, 9 is 0, 8 is 1, 7 is 2, 6 is 3, <6 is 4

if 90 < grade <= 100:
    grade = "A"
elif 80 < grade <= 89:
    grade = "B"