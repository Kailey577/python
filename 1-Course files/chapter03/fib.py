
def fib(n):
    
    if n == 1:
        return 1
    if n == 0:
        return 0
    return fib(n-1) + fib(n-2)

for i in range(100):
    print(f"i={i}\t{fib(i)}")


f1= 1
f2 = 0
## loop to calculate nth fib
## update f1 and f2 approp