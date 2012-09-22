"""
    shell_sort.py

    This module implements shell sort on an unsorted list and returns a sorted list.

    Shell Sort Overview:
    ------------------------
    Comparision sort that sorts far away elements first to sort the list

    Pre: an unsorted list[0,...,n] of integers.

    Post: returns a sorted list[0,...,n] in ascending order.

    Time Complexity:  O(n^2)

    Space Complexity: O(n)

    Stable: Yes

    Psuedo Code: http://en.wikipedia.org/wiki/Shell_sort

    shell_sort.sort(list) -> sorted_list
"""


def sort(seq):

    gaps = [x for x in range(len(seq) / 2, 0, -1)]

    for gap in gaps:
        for i in range(gap, len(seq)):
            temp = seq[i]
            j = i
            while j >= gap and seq[j - gap] > temp:
                seq[j] = seq[j - gap]
                j -= gap
            seq[j] = temp

    return seq
