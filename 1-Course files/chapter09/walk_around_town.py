from random import randint
from math import sqrt



def walk(n: int)->float:
    x = y = 0
    for _ in range(n):
        #walk around
        roll = randint(1,4)
        if roll == 1: x+=1
        elif roll == 2: x-=1
        elif roll == 3: y+= 1
        else: y-= 1
    return sqrt(x**2 + y**2)

def main():
    print(walk(10000))


if __name__=="__main__": main()
