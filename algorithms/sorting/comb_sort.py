"""
    comb_sort.py

    This module implements comb sort on an unsorted list and returns a sorted list.

    Comb Sort Overview:
    -------------------
    Improves on bubble sort by using a gap sequence to remove turtles.

    Pre: an unsorted list[0,...,n] of integers.

    Post: returns a sorted list[0,...,n] in ascending order.

    Time Complexity: O(n^2)

    Space Complexity: O(n) total

    Stable: Yes

    Psuedo code: http://en.wikipedia.org/wiki/Comb_sort

    comb_sort.sort(list) -> sorted_list

"""
def sort(seq):
   gap = len(seq)
   swap = True
   
   while gap > 1 or swap:
       gap = max(1, int( gap / 1.25))
       swap = False
       for i in range(len(seq) - gap):
           if seq[i] > seq[i + gap]:
               seq[i], seq[i + gap] = seq[i + gap], seq[i]
               swap = True
   return seq 
