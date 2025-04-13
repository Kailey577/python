
from random import random, randrange


'''dart_amount = int(input("Enter the number of darts thrown"))'''


def throw_dart() -> [int, int]:
    # randomly throw a dart
    l = []
    for i in range(2):
        l.append(2*random())
    return l

darts_in_circle = 0
darts_on_cabinet = 0
number_of_darts = 100000
for i in range(number_of_darts):
    x_coord = 2*random()-1
    y_coord = 2*random()-1
    if (x_coord*x_coord)+(y_coord*y_coord) <= 1:
        darts_in_circle += 1
    else:
        darts_on_cabinet += 1

    print(x_coord, y_coord)
    print(darts_on_cabinet, darts_in_circle)
pi = 4*(darts_in_circle/number_of_darts)
print(pi)