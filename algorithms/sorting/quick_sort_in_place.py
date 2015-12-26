"""
    Quick Sort in Place
    -------------------
    Uses partitioning to recursively divide and sort the list

    Time Complexity: O(n**2) worst case

    Space Complexity: O(log n) this version

    Stable: No

    Psuedo Code: http://rosettacode.org/wiki/Quick_Sort

"""
from random import randrange


def partition(seq, left, right, pivot_index):
    """
    Reorders the slice with values lower than the pivot at the left side,
    and values bigger than it at the right side.
    Also returns the store index.

    :param seq: A list of integers
    :param left: An integer representing left index
    :param right: An integer representing left index
    :param pivot_index: An integer that we're pivoting off
    :rtype: An stored_index integer
    """
    pivot_value = seq[pivot_index]
    seq[pivot_index], seq[right] = seq[right], seq[pivot_index]
    store_index = left
    for i in range(left, right):
        if seq[i] < pivot_value:
            seq[i], seq[store_index] = seq[store_index], seq[i]
            store_index += 1
    seq[store_index], seq[right] = seq[right], seq[store_index]
    return store_index


def sort(seq, left, right):
    """
    Takes a list of integers and sorts them in ascending order. This sorted
    list is then returned.

    :param seq: A list of integers
    :param left: An integer representing the beginning index
    :param right: An integer representing the end index
    :rtype: A list of sorted integers
    """

    if len(seq) <= 1:
        return seq
    elif left < right:
        pivot = randrange(left, right)
        pivot_new_index = partition(seq, left, right, pivot)
        sort(seq, left, pivot_new_index - 1)
        sort(seq, pivot_new_index + 1, right)
        return seq
