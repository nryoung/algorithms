"""
    insertion_sort.py

    Implemenation of insertion sort on a list and returns a sorted list.

    Insertion Sort Overview:
    ------------------------
    Uses insertion of elements in to the list to sort the list.

    Time Complexity: O(n**2)

    Space Complexity: O(n) total

    Stable: Yes

    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed.

"""


def sort(seq):
    for n in range(1, len(seq)):
        item = seq[n]
        hole = n
        while hole > 0 and seq[hole - 1] > item:
            seq[hole] = seq[hole - 1]
            hole = hole - 1
        seq[hole] = item
    return seq
