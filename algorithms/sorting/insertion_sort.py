"""
    insertion_sort.py
    
    This module implements insertion sort on an unsorted list and returns a sorted list.
    
    Insertion Sort Overview:
    ------------------------
    Uses insertion of elements in to the list to sort the list.
    
    Pre: an unsorted list[0,...,n] of integers.

    Post: returns a sorted list[0,...,n] in ascending order.

    Time Complexity: O(n^2)

    Space Complexity: O(n) total

    Stable: Yes

    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed. 

    insertion_sort.sort(list) -> sorted_list  
"""
def sort(seq):
    for n in range(1, len(seq)):
        item = seq[n]
        hole = n
        while hole > 0 and seq[ hole - 1] > item:
            seq[hole] = seq[hole - 1]
            hole = hole - 1
        seq[hole] = item
    return seq
