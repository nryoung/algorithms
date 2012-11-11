"""
    bogo_sort.py

    Implementation of bogo sort on a list and returns a sorted list.

    Bogo Sort Overview:
    -------------------
    A naive sorting that picks two elements at random and swaps them.

    Time Complexity: O(n * n!)

    Space Complexity: O(1) Auxiliary

    Stable: No

    WARNING: This algorithm may never sort the list correctly.
"""

import random


def sort(seq):
    if len(seq) == 1:
        return seq
    random.seed()
    while not is_sorted(seq):
        if len(seq) == 2:
            i = 0
            j = 1
        else:
            i = random.randint(0, len(seq) - 2)
            j = random.randint(i, len(seq) - 1)
        seq[i], seq[j] = seq[j], seq[i]
    return seq


def is_sorted(seq):
    return all(seq[i - 1] <= seq[i] for i in xrange(1, len(seq)))
