"""
    bubble_sort.py

    This module implements bubble sort on an unsorted list and returns the sorted list.

    Bubble Sort Overview:
    ---------------------
    A naive sorting that compares and swaps adjacent elements from 0,1,2,...,n.

    Pre: an unsorted list[0,...,n] of integers.

    Post: returns a sorted list[0,...,n] in ascending order.

    Time Complexity: O(n^2)

    Space Complexity: O(n) total

    Stable: Yes

    Psuedo code: http://en.wikipedia.org/wiki/Bubble_sort

    bubble_sort.sort(list) -> sorted_list

"""


def sort(seq):

    for x in seq:
        temp = 0
        for n in range(1, len(seq)):
            temp = seq[n]
            if seq[n] < seq[n - 1]:
                seq[n] = seq[n - 1]
                seq[n - 1] = temp
    return seq
