"""
    merge_sort.py

    Implementation of merge sort on a list and returns a sorted list.

    Merge Sort Overview:
    ------------------------
    Uses divide and conquer to recursively divide and sort the list

    Time Complexity: O(n log n)

    Space Complexity: O(n) Auxiliary

    Stable: Yes

    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed.

"""


def merge(left, right):
    result = []
    n, m = 0, 0
    while n < len(left) and m < len(right):
        if left[n] <= right[m]:
            result.append(left[n])
            n += 1
        else:
            result.append(right[m])
            m += 1

    result += left[n:]
    result += right[m:]
    return result


def sort(seq):
    if len(seq) <= 1:
        return seq

    middle = len(seq) / 2
    left = sort(seq[:middle])
    right = sort(seq[middle:])
    return merge(left, right)
