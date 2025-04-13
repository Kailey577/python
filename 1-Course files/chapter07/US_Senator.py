age_input = input("WHAT IS YOUR AGE: ")
years_of_citizenship = input("HOW MANY YEARS OF CITIZENSHIP: ")

if int(age_input) >= 30:
    if int(years_of_citizenship) >= 9:
        print("you can be a senator and representative")
        quit()
    if int(years_of_citizenship) >= 7:
        print("you can be a representative")
        quit()
    else:
        print("you cannot be a representative or senator")
        quit()
elif int(age_input)>=25:
    if int(years_of_citizenship) >= 7:
        print("You can be a representative")
        quit()
    print("you cannot be a representative or senator")

print("you cannot be a representative or senator")
quit()



