import math
a=0
sign=1
n = eval(input("how many terms will be summed?: "))
for i in range(1,n+1, 2):
 a += 4/i*sign

 sign = sign*-1

#4/1-4/(1+k)+4/(3+k)-4/(5+k)
print(a)