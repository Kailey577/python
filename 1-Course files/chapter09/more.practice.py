from random import random, randrange


def throw_dart() -> [int, int]:
    # randomly throw a dart
    l = []
    for i in range(2):
        l.append(2*random())
    return l


