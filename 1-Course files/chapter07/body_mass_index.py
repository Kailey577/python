#
LOWEST_BMI = 19

HIGHEST_BMI = 25

weight = int(input("enter weight"))
height = int(input("enter height"))

BMI = (weight*720)/(height*height)

if BMI < LOWEST_BMI :
    print("YOU ARE BELOW HEALTHY RANGE")
    exit()

if BMI > HIGHEST_BMI :
    print("YOU ARE ABOVE HEALTHY RANGE")
    exit()

print(" YOU ARE IN HEALTHY RANGE ")