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
    pattern_length = len(pattern)
    text_length = len(text)
    offsets = []
    if pattern_length > text_length:
        return offsets
    bmbc = [pattern_length] * 256
    for k, p in enumerate(pattern[:-1]):
        bmbc[ord(p)] = pattern_length - k - 1
    bmbc = tuple(bmbc)
    k = pattern_length - 1
    while k < text_length:
        j = pattern_length - 1
        i = k
        while j >= 0 and text[i] == pattern[j]:
            j -= 1
            i -= 1
        if j == -1:
            offsets.append(i + 1)
        k += bmbc[ord(text[k])]

    return offsets
