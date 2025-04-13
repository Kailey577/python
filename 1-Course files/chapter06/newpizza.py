

def price(p_rce = float)->float:
    square_inch = p_rce/(3.14 * d_meter/2*d_meter/2)
    return square_inch

#...........
def price(p_rce):
    per = p_rce / (3.14 * d_meter/2*d_meter/2)
    print("the price per square inch is " + str(per))

def areaa(d_meter = float)->float:
    '''finds area of pizza'''
    area = (d_meter/2)**2*3.14
    return area
assert areaa(3) == (3/2)*(3/2)*3.14
assert areaa(4) == 2*2*3.14
#...........
def areaa(d_meter):
    radius = d_meter / 2
    area = 3.14 * (radius * radius)
    print("the area of the pizza is " + str(area) + " square inches")
#.............
d_meter = float(input("enter the diameter of pizza(inches):"))
p_rce = float(input("Enter the price of the pizza: "))
areaa(d_meter)
price(p_rce)