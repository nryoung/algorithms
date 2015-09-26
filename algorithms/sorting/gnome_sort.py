"""
    gnome_sort.py

    Implementation of gnome sort on a list and returns a sorted list.

    Gnome Sort Overview:
    ---------------------
    A sorting algorithm similar to insertion sort except that the element is
    moved to its proper place by a series of swaps.

    Time Complexity: O(n^2)

    Space Complexity: O(1) auxillary

    Stable: No

    Psuedo code: http://en.wikipedia.org/wiki/Gnome_sort

"""


def sort(seq):

    i = 1
    last = 0
    while i < len(seq):
        if seq[i] < seq[i-1]:
            seq[i], seq[i-1] = seq[i-1], seq[i]
            if i > 1:
                if last == 0:
                    last = i
                i -= 1
            else:
                i += 1
        else:
            if last != 0:
                i = last
                last = 0
            i += 1
    return seq
