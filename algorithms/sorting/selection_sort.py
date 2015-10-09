"""
    Selection Sort
    --------------
    A sorting that uses in-place comparison.

    Time Complexity:  O(n**2)

    Space Complexity: O(1) Auxiliary

    Stable: Yes

    Psuedo Code: http://en.wikipedia.org/wiki/Selection_sort

"""


def sort(seq):
    """
    Takes a list of integers and sorts them in ascending order. This sorted
    list is then returned.

    :param seq: A list of integers
    :rtype: A list of sorted integers
    """
    for i in range(0, len(seq)):
        iMin = i
        for j in range(i+1, len(seq)):
            if seq[iMin] > seq[j]:
                iMin = j
        if i != iMin:
            seq[i], seq[iMin] = seq[iMin], seq[i]

    return seq
