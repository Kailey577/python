k = []
howmany = int(input("How many numbers?: "))
print(howmany)
for i in range(1,howmany+1):
    number = eval(input("Enter a number: "))
    k.append(number)
result = sum(k)
lastresult = result/howmany
print("the average is", lastresult)