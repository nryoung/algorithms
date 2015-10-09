"""
    strand_sort.py

    Implementation of strand sort on a list and returns a sorted list.

    Strand Sort Overview:
    ------------------------
    Repeatedly pulls sorted sublists out of the unsorted list and merges them
    with a result array.

    Time Complexity: O(n**2) worst case

    Space Complexity: O(1) auxiliary

    Stable: Yes

    Psuedo Code: https://en.wikipedia.org/wiki/Strand_sort
"""

from collections import deque


def sort(array):
    if len(array) < 2:
        return array
    result = []
    while array:
        sublist = [array.pop()]
        last = sublist[0]
        sub_append = sublist.append
        leftovers = deque()
        left_append = leftovers.append
        for item in array:
            if item >= last:
                sub_append(item)
                last = item
            else:
                left_append(item)
        result = merge(result, sublist)
        array = leftovers
    return result


def merge(left, right):
    merged_list = []
    merged_list_append = merged_list.append

    it_left = iter(left)
    it_right = iter(right)

    left = next(it_left, None)
    right = next(it_right, None)

    while left is not None and right is not None:
        if left > right:
            merged_list_append(right)
            right = next(it_right, None)
        else:
            merged_list_append(left)
            left = next(it_left, None)

    if left:
        merged_list_append(left)
        merged_list.extend(i for i in it_left)
    else:
        merged_list_append(right)
        merged_list.extend(i for i in it_right)

    return merged_list
