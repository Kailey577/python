
#2. Writeaprogramthatcalculatesthecostpersquareinchofacircularpizza,
#given its diameter and price.
#The formula for area is A= 1rr2•

diameter = float(input("Enter the diameter of the pizza (inches): "))
radius = diameter/2
price = float(input("Enter the price of the pizza: "))
area = 3.14*(radius*radius)
per = price/area
print("the area of the pizza is " + str(area)+" square inches")
print("the price per square inch is "+str(per))

`