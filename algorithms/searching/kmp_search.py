"""
    kmp_search.py
    
    This module implements kmp search on a sorted list.
    
    KMP Search Overview:
    ------------------------
    Uses a prefix function to reduce the searching time.
     
    Pre: a sorted list[0,...n,] integers and the key to search for.

    Post: returns the index of where the first element that matches the key.

    Time Complexity:  O(n + k), where k is the substring to be found

    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed. 
    kmp_search.search(sorted_list) -> integer
    kmp_search.search(sorted_list) -> False
"""

def search(string, word):
    n = len(string)
    m = len(word)
    pi = compute_prefix(word)
    q = 0
    for i in range(n):
        while q > 0 and word[q] != string[i]:
            q = pi[q - 1]
        if word[q] == string[i]:
            q = q + 1
        if q == m:
            return i - m + 1
    return False

def compute_prefix(word):
    m = len(word)
    pi = [0] * m
    k = 0

    for q in range(1, m):
        while k > 0 and word[k] != word[q]:
            k = pi[k - 1]
        
        if word[k + 1] == word[q]:
            k = k + 1
        pi[q] = k
    return pi
