"""
    Insertion Sort
    --------------
    A sort that uses the insertion of elements in to the list to sort the list.

    Time Complexity: O(n**2)

    Space Complexity: O(n) total

    Stable: Yes

    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed.

"""


def sort(seq):
    """
    Takes a list of integers and sorts them in ascending order. This sorted
    list is then returned.

    :param seq: A list of integers
    :rtype: A list of integers
    """
    for n in range(1, len(seq)):
        item = seq[n]
        hole = n
        while hole > 0 and seq[hole - 1] > item:
            seq[hole] = seq[hole - 1]
            hole = hole - 1
        seq[hole] = item
    return seq
