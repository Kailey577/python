from functools import total_ordering
from random import randint

def walk(n: int)->int:
    #produces distance from starting point after n random steps
    distance = 0
    for i in range(n):
        distance += 1 if randint(1,2) == 1 else -1
    return distance

def simulate(num_trials: int, walk_steps: int) -> float:
    '''
    returns average distance from origin in a random walk
    with walk_steps
    '''
    total_distance = 0
    for _ in range(num_trials):
        total_distance += walk(walk_steps)
    return total_distance / num_trials


def main():
    t = eval(input("number of trials:"))
    n = eval(input("walk steps: "))
    print(f"On average you were {simulate(t,n)} from the origin")


if __name__=="__main__":
    main()