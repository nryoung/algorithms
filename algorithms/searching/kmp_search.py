"""
    kmp_search.py

    This module implements kmp search on a sorted list.

    KMP Search Overview:
    ------------------------
    Uses a prefix function to reduce the searching time.

    Pre: a string > substring.

    Post: returns a list of indices where the substring was found.

    Time Complexity:  O(n + k), where k is the substring to be found

    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed.

    kmp_search.search(sorted_list) -> integer
    kmp_search.search(sorted_list) -> False
"""


def search(string, word):
    word_length = len(word)
    prefix = compute_prefix(word)
    q = 0
    for i in xrange(len(string)):
        while q > 0 and word[q] != string[i]:
            q = prefix[q - 1]
        if word[q] == string[i]:
            q = q + 1
        if q == word_length:
            return i - word_length + 1
    return False


def compute_prefix(word):
    word_length = len(word)
    prefix = [0] * word_length
    k = 0

    for q in xrange(1, word_length):
        while k > 0 and word[k] != word[q]:
            k = prefix[k - 1]

        if word[k + 1] == word[q]:
            k = k + 1
        prefix[q] = k
    return prefix
