"""
    bubble_sort.py

    Implementation of bubble sort on a list and returns a sorted list.

    Bubble Sort Overview:
    ---------------------
    A naive sorting that compares and swaps adjacent elements

    Time Complexity: O(n**2)

    Space Complexity: O(1) Auxiliary

    Stable: Yes

    Psuedo code: http://en.wikipedia.org/wiki/Bubble_sort

"""


def sort(seq):
    L = len(seq)
    for _ in range(L):
        for n in range(1, L):
            if seq[n] < seq[n - 1]:
                seq[n - 1], seq[n] = seq[n], seq[n - 1]
    return seq
