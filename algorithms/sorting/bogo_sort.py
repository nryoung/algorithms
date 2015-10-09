"""
    Bogo Sort
    ---------
    A naive sorting that picks two elements at random and swaps them.

    Time Complexity: O(n * n!)

    Space Complexity: O(1) Auxiliary

    Stable: No

    Psuedo code: None

    **WARNING**: This algorithm may never sort the list correctly.
"""

import random


def sort(seq):
    """
    Takes a list of integers and sorts them in ascending order. This sorted
    list is then returned.

    :param seq: A list of integers
    :rtype: A list of sorted integers
    """

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
    """
    Takes a list of integers and checks if the list is in sorted order.

    :param seq: A list of integers
    :rtype: Boolean
    """
    return all(seq[i - 1] <= seq[i] for i in range(1, len(seq)))
