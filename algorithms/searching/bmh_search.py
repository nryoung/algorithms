"""
    bmh_search.py

    This module implements bmh search to find a substring in a string

    BMH Search Overview:
    --------------------
    Uses a bad-character shift of the rightmost character of the window to
    compute shifts.

    Pre: a string > substring.

    Post: returns a list of indexes where the substring was found.

    Time: Complexity: O( m + n), where m is the substring to be found.

    Space: Complexity: O(m), where m is the substring to be found.

    Psuedo Code: https://github.com/FooBarWidget/boyer-moore-horspool
                 (converted from C++)

    bmh_search.search(string, substring) -> list[integers]
    bmh_search.search(string, substring) -> list[empty]
"""


def search(text, pattern):
    m = len(pattern)
    n = len(text)
    offsets = []
    if m > n:
        return offsets
    bmbc = []
    for k in range(256):
        bmbc.append(m)
    for k in range(m - 1):
        bmbc[ord(pattern[k])] = m - k - 1
    bmbc = tuple(bmbc)
    k = m - 1
    while k < n:
        j = m - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            offsets.append(i + 1)
        k += bmbc[ord(text[k])]

    return offsets
