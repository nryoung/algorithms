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

    kmp_search.search(sorted_list) -> list[integers]
    kmp_search.search(sorted_list) -> list[empty]
"""


def search(string, word):
    word_length = len(word)
    string_length = len(string)
    prefix = compute_prefix(word)
    offsets = []
    if word_length > string_length:
        return offsets
    q = 0 # q is the number of characters matched
    for i in xrange(string_length):
        while q > 0 and word[q] != string[i]:
            q = prefix[q - 1] # next character does not match
        if word[q] == string[i]:
            q += 1
        if q == word_length:
            offsets.append(i - word_length + 1)
            q = prefix[q - 1] # look for next match
    return offsets


def compute_prefix(word):
    word_length = len(word)
    prefix = [0 for i in xrange(word_length)]
    k = 0

    for q in xrange(1, word_length):
        while k > 0 and word[k] != word[q]:
            k = prefix[k - 1]

        if word[k + 1] == word[q]:
            k = k + 1
        prefix[q] = k
    return prefix
