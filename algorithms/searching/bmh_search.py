"""
    bmh_search.py

    This module implements bmh search to find a substring in a string

    BMH Search Overview:
    --------------------
    Uses a bad-character shift of the rightmost character of the window to
    compute shifts.

    Pre: a string > substring.

    Post: returns a list of indexes where the substring was found.

    Time: Complexity: O(m + n), where m is the substring to be found.

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
    # bmbc is a lookup-tuple of "skip values"
    # if we're looking at an index of text, and we
    # can't find part of pattern there, we can safely
    # skip back up to pattern_length characters
    bmbc = [pattern_length] * 256
    # if we do find part of pattern there, but it's a
    # failed search at that index, we jump back
    # (pattern_length - index - 1) characters
    for index, char in enumerate(pattern[:-1]):
        bmbc[ord(char)] = pattern_length - index - 1
    bmbc = tuple(bmbc)
    search_index = pattern_length - 1
    while search_index < text_length:
        pattern_index = pattern_length - 1
        text_index = search_index
        while text_index >= 0 and
              text[text_index] == pattern[pattern_index]:
            pattern_index -= 1
            text_index -= 1
        if pattern_index == -1:
            offsets.append(text_index + 1)
        search_index += bmbc[ord(text[search_index])]

    return offsets
