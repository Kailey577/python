'''1. Write a program to calculate the volume and surface area of a sphere from its radius,
 given as input. Here are some formulas that might be useful:
V= 4/37rr3 A= 47rr2'''

radius = eval(input('Enter the radius of the sphere : '))

volume = 4/3*3.14*radius**3
area = 4*3.14*radius*radius

print(volume)
print(area)