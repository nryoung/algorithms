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

    binary_search.search(sorted_list) -> integer
    binary_search.search(sorted_list) -> False
"""


def search(seq, key):
    imin = 0
    imax = len(seq) - 1

    if imax < imin:
        return False

    else:
        mid = len(seq) / 2

        if seq[mid] > key:
            return search(seq[:mid - 1], key)

        elif seq[mid] < key:
            return search(seq[mid + 1:], key)

        else:
            return mid
