"""
    Comb Sort
    ---------
    Improves on bubble sort by using a gap sequence to remove turtles.

    Time Complexity: O(n**2)

    Space Complexity: O(1) Auxiliary

    Stable: Yes

    Psuedo code: http://en.wikipedia.org/wiki/Comb_sort

"""


def sort(seq):
    """
    Takes a list of integers and sorts them in ascending order. This sorted
    list is then returned.

    :param seq: A list of integers
    :rtype: A list of sorted integers
    """

    gap = len(seq)
    swap = True

    while gap > 1 or swap:
        gap = max(1, int(gap / 1.25))
        swap = False
        for i in range(len(seq) - gap):
            if seq[i] > seq[i + gap]:
                seq[i], seq[i + gap] = seq[i + gap], seq[i]
                swap = True
    return seq
