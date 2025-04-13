k = []
howmany = int(input("How many numbers are to be summed?: "))
print(howmany)
for i in range(1,howmany+1):
    number = eval(input("Enter a number: "))
    k.append(number)
print("here is the sum: ", sum(k))