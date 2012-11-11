"""
    binary_search.py

    Implementation of binary search on a sorted list.

    Binary Search Overview:
    ------------------------
    Recursively partitions the list until the key is found.

    Time Complexity:  O(lg n)

    Psuedo Code: http://en.wikipedia.org/wiki/Binary_search

"""


def search(seq, key):
    lo = 0
    hi = len(seq) - 1

    while hi >= lo:
        mid = lo + (hi - lo) // 2
        if seq[mid] < key:
            lo = mid + 1
        elif seq[mid] > key:
            hi = mid - 1
        else:
            return mid
    return False
