"""
    quick_sort.py
    
    This module implements quick sort on an unsorted list and returns a sorted list.
    
    Quick Sort Overview:
    ------------------------
    Uses partitioning to recursively divide and sort the list
     
    Pre: an unsorted list[0,...,n] of integers.

    Post: returns a sorted list[0,...,n] in ascending order.

    Time Complexity: O(n log n) average, O(n^2) worst case

    Space Complexity: O(n) 

    Stable: No

    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed. 

    quick_sort.sort(list) -> sorted_list  
"""

def sort(seq):
   
   if len(seq) < 1:
       return seq
   else:
       pivot = seq[0]
       left = sort([x for x in seq[1:] if x < pivot])
       right = sort([x for x in seq[1:] if x >= pivot])
       return left + [pivot] + right
