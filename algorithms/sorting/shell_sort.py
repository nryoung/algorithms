"""
    shell_sort.py

    Implementation of shell sort on an list and returns a sorted list.

    Shell Sort Overview:
    ------------------------
    Comparision sort that sorts far away elements first to sort the list

    Time Complexity:  O(n**2)

    Space Complexity: O(1) Auxiliary

    Stable: Yes

    Psuedo Code: http://en.wikipedia.org/wiki/Shell_sort

"""


def sort(seq):

    gaps = [x for x in range(len(seq) // 2, 0, -1)]

    for gap in gaps:
        for i in range(gap, len(seq)):
            temp = seq[i]
            j = i
            while j >= gap and seq[j - gap] > temp:
                seq[j] = seq[j - gap]
                j -= gap
            seq[j] = temp

    return seq
