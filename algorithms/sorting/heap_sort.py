"""
    Heap Sort
    ---------
    Uses the max heap data structure implemented in a list.

    Time Complexity: O(n log n)

    Space Complexity: O(1) Auxiliary

    Stable: Yes

    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed.

"""


def max_heapify(seq, i, n):
    """
    The function of max_heapify is to let the value at seq[i] "float down" in
    the max-heap so that the subtree rooted at index i becomes a max-heap.

    :param seq: A list of integers
    :param i: An integer that is an index in to the list that represents the
              root of a subtree that max heapify is called on.
    :param n: length of the list
    """
    l = 2 * i + 1
    r = 2 * i + 2

    if l <= n and seq[l] > seq[i]:
        largest = l
    else:
        largest = i
    if r <= n and seq[r] > seq[largest]:
        largest = r

    if largest != i:
        seq[i], seq[largest] = seq[largest], seq[i]
        max_heapify(seq, largest, n)


def build_heap(seq):
    """
    Continously calls max_heapify on the list for each subtree.

    :param seq: A list of integers
    """
    n = len(seq) - 1
    for i in range(n//2, -1, -1):
        max_heapify(seq, i, n)


def sort(seq):
    """
    Takes a list of integers and sorts them in ascending order. This sorted
    list is then returned.

    :param seq: A list of integers
    :rtype: A list of sorted integers
    """
    build_heap(seq)
    heap_size = len(seq) - 1
    for x in range(heap_size, 0, -1):
        seq[0], seq[x] = seq[x], seq[0]
        heap_size = heap_size - 1
        max_heapify(seq, 0, heap_size)

    return seq
