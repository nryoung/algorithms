"""
    knuth.py
    Implementation of the Fisher-Yates/Knuth shuffle

    Pre: Takes any list, unshuffled
    Post: Returns list shuffled randomly

    Time Complexity: n
    Space Complexity: n

    Pseudocode: http://en.wikipedia.org/wiki/Fisher%E1%80%93Yates_shuffle

"""
from random import seed, randint


def shuffle(seq):
    seed()
    for i in reversed(range(len(seq))):
        j = randint(0, i)
        seq[i], seq[j] = seq[j], seq[i]
    return seq
