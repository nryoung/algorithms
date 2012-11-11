"""
    selection_sort.py

    Implementation of selection sort on a list and returns a sorted list.

    Selection Sort Overview:
    ------------------------
    Uses in-place comparision to sort the list

    Time Complexity:  O(n**2)

    Space Complexity: O(1) Auxiliary

    Stable: Yes

    Psuedo Code: http://en.wikipedia.org/wiki/Selection_sort

"""


def sort(seq):

    for i in range(0, len(seq)):
        minat = i
        minum = seq[i]
        for j in range(i + 1, len(seq)):
            if minum > seq[j]:
                minat = j
                minum = seq[j]
        temp = seq[i]
        seq[i] = seq[minat]
        seq[minat] = temp

    return seq
