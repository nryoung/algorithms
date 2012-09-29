"""
    binary_search.py

    This module implements binary search on a sorted list.

    Binary Search Overview:
    ------------------------
    Recursively partitions the list until the key is found.

    Pre: a sorted list[0,...n,] integers and the key to search for.

    Post: returns the index of where the first element that matches the key.

    Time Complexity:  O(lg n)

    Psuedo Code: http://en.wikipedia.org/wiki/Binary_search

    binary_search.search(sorted_list, key) -> index
    binary_search.search(sorted_list, key) -> False
"""


def search(seq, key):
    lo = 0
    hi = len(seq)

    while hi >= lo:
        mid = (lo + hi) / 2
        if seq[mid] < key:
            lo = mid + 1
        elif seq[mid] > key:
            hi = mid 
        else:
            return mid
    return False
