'''The Konditorei coffee shop sells coffee at $10.50 a pound plus the cost of shipping. Each order ships for $0.86 per pound + $1.50 fixed cost for overhead. Write a program that calculates
 the cost of an order.'''

pounds = float(input("How many pounds of coffee would you like to order?"))

total_cost = pounds * 10.5 + pounds * 0.86 + 1.50

print("Your order cost is "+"$"+str(total_cost)+".")
