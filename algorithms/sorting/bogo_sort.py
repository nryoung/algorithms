"""
        bogo_sort.py

        This module implements bogo sort on an unsorted list and
        returns the list in sorted order.

        Bogo Sort Overview:
        -------------------
        If list is not in order, picks two elements at random and swaps them.
        Repeat.

    Pre:

    Time Complexity: O(n * n!)

    Space Complexity: O(n) total

    Stable: No

    bogo_sort.sort(list) -> sorted_list

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
    for i in xrange(1, len(seq)):
        if seq[i - 1] > seq[i]:
            return False
    return True
