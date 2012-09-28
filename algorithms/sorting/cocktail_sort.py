"""
    cocktail_sort.py

    This module implements a cocktail sort (aka bidirectional bubble sort,
    or the happy hour sort) on an unsorted list.

    Cocktail Sort Overview:
    ------------------------
    Walk the list bidirectionally, swapping neighbors if one should come
    before/after the other.

    Pre: An unsorted list elements that can be compared.

    Post: A sorted list of elements in ascending order.

    Time Complexity: O(n^2)

    Space Complexity: O(n) total

    Stable: Yes

    Psuedo Code: http://en.wikipedia.org/wiki/Cocktail_sort
    cocktail_sort.sort(list) -> sorted_list
"""


def sort(seq):
    lower_bound = -1
    upper_bound = len(seq) - 1
    swapped = True
    while swapped:
        swapped = False
        lower_bound += 1
        for i in range(lower_bound, upper_bound):
            if seq[i] > seq[i + 1]:
                seq[i], seq[i + 1] = seq[i + 1], seq[i]
                swapped = True
        if not swapped:
            break
        swapped = False
        upper_bound -= 1
        for i in range(upper_bound, lower_bound, -1):
            if seq[i] < seq[i - 1]:
                seq[i], seq[i - 1] = seq[i - 1], seq[i]
                swapped = True
    return seq
