"""
    quick_sort_in_place.py

    Implementation of quick sort on a list and returns a sorted list.
    In-place version.

    Quick Sort Overview:
    ------------------------
    Uses partitioning to recursively divide and sort the list

    Time Complexity: O(n**2) worst case

    Space Complexity: O(log n) this version

    Stable: No

    Psuedo Code: http://en.wikipedia.org/wiki/Quicksort#In-place_version

"""
from random import randrange


def partition(seq, left, right, pivot_index):
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
    """in-place version of quicksort"""
    if len(seq) <= 1:
        return seq
    elif left < right:
        # pivot = (left+right)/2
        pivot = randrange(left, right)
        pivot_new_index = partition(seq, left, right, pivot)
        sort(seq, left, pivot_new_index - 1)
        sort(seq, pivot_new_index + 1, right)
        return seq
