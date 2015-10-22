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


def sort(array):
    if len(array) < 2:
        return array
    result = []
    while array:
        sublist = [array.pop(0)]
        leftovers = []
        last = sublist[0]
        # For speed, frequently invoked functions are assigned to locally-
        # scoped variables, which greatly reduces overhead in calling them.
        sublist_append = sublist.append
        leftovers_append = leftovers.append
        for item in array:
            if item >= last:
                sublist_append(item)
                last = item
            else:
                leftovers_append(item)
        result = merge(result, sublist)
        array = leftovers
    return result


def merge(left, right):
    if not left:
        return right
    if not right:
        return left

    if left[-1] > right[-1]:
        left, right = right, left

    it = iter(right)
    y = next(it)
    result = []

    for x in left:
        while y < x:
            result.append(y)
            y = next(it)
        result.append(x)
    result.append(y)
    result.extend(it)
    return result
