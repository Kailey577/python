
import math
import pytest



def is_prime(n: int) -> bool:
    # produces true if n is prime
    if n < 2: return False
    for i in range(2, int(math.sqrt(n)+1)):
        if n % i == 0: return False
    return True



def prime_finder(n: int) -> [int]:
    # produces list of all primes <= n
    primes = []
    for i in range(2, n+1):
        if is_prime(i):
            primes.append(i)
    return primes

def test():
    assert not is_prime(14)
    p_less_twenty = [2,3,5,7,11,13,17,19]
    for p in p_less_twenty: assert is_prime(p)


    assert prime_finder(2) == [2]
    assert prime_finder(20) == p_less_twenty
    assert prime_finder(0) == []


def main():
    user_input = int(input("Enter your number: "))
    number = user_input

    while number >= 1:
        prime_finder(number)
        number -= 1


#main()