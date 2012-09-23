"""
    heap_sort.py

    This module implements heap sort on an unsorted list and returns a sorted list.

    Heap Sort Overview:
    -------------------
    Uses a the max heap data structure implemented in a list.

    Pre: an unsorted list[0,...,n] of integers.

    Post: returns a sorted list[0,...,n] in ascending order.

    Time Complexity: O(n^2)

    Space Complexity: O(n) total

    Stable: Yes

    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed.

    heap_sort.sort(list) -> sorted_list

"""


def max_heapify(seq, i, n):
    l = i + 1
    r = i + 2

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
    n = len(seq) - 1
    for i in range(n, -1, -1):
        max_heapify(seq, i, n)


def sort(seq):
    build_heap(seq)
    heap_size = len(seq) - 1
    for x in range(heap_size, -1, -1):
        seq[0], seq[x] = seq[x], seq[0]
        heap_size = heap_size - 1
        max_heapify(seq, 0, heap_size)

    return seq
