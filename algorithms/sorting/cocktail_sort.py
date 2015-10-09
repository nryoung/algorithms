"""
    Cocktail Sort
    -------------
    A bidirectional bubble sort. Walks the elements bidirectionally, swapping
    neighbors if one should come before/after the other.

    Time Complexity: O(n**2)

    Space Complexity: O(1) Auxiliary

    Stable: Yes

    Psuedo Code: http://en.wikipedia.org/wiki/Cocktail_sort

"""


def sort(seq):
    """
    Takes a list of integers and sorts them in ascending order. This sorted
    list is then returned.

    :param seq: A list of integers
    :rtype: A list of sorted integers
    """

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
