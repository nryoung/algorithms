"""
    knuth.py
    Implementation of the Fisher-Yates/Knuth shuffle

    Fisher-Yates/Knuth Overview:
    ----------------------------
    Randomly picks integers to swap elements in an ubiased manner.

    Time Complexity: O(n)
    Space Complexity: O(n)n

    Pseudocode: http://en.wikipedia.org/wiki/Fisher%E1%80%93Yates_shuffle

"""
from random import seed, randint


def shuffle(seq):
    seed()
    for i in reversed(range(len(seq))):
        j = randint(0, i)
        seq[i], seq[j] = seq[j], seq[i]
    return seq
