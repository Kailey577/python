import math

x1 = eval(input("please enter the first point(x): "))
y1 = eval(input("please enter the first point(y): "))

x2 = eval(input("please enter the second point(x): "))
y2 = eval(input("please enter the second point(y): "))


print("let's find the distance between these two points!")
distance = math.sqrt((x2-x1)**2+(y2-y1)**2)
print ("the distance between these two points is:", distance)