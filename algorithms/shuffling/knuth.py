"""
    Fisher-Yates/Knuth
    ------------------
    Randomly picks integers to swap elements in an ubiased manner.

    Time Complexity: O(n)

    Space Complexity: O(n)n

    Pseudocode: http://http://rosettacode.org/wiki/Knuth_shuffle

"""
from random import seed, randint


def shuffle(seq):
    """
    Takes a list of integers and randomly swaps the elements in an unbiased
    manner.

    :param seq: A list of integers
    :rtype: A list of shuffled integers
    """
    seed()
    for i in reversed(range(len(seq))):
        j = randint(0, i)
        seq[i], seq[j] = seq[j], seq[i]
    return seq
