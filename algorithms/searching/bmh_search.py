"""
    bmh_search.py

    This module implements bmh search to find a substring in a string

    BMH Search Overview:
    --------------------
    Uses a bad-character shift of the rightmost character of the window to
    compute shifts.

    The trick to this algorithm is `bmbc`, a lookup table with a default
    value equal to the length of the pattern to be searched, so that
    the algorithm can skip `len(pattern)` indices through the string
    for efficiency's sake. For example, if we're searching through the
    string "cotton milled paper" for the pattern "grumble", we look at
    the last letter "r" (BMH goes backwards through a string) and notices
    that it is not equal to "e". Thus, we can afford to jump our search
    index back a whole seven characters.

    However, not all the entries in `bmbc` are equal to `len(pattern)`.
    If we searched the string "adventure time" for "grumble", we'd find
    the "e" to match but mismatch the "m" and "l" in the string and
    pattern, respectively. In this case, we can only jump back six
    characters safely, which is why `bmbc` contains values that are not
    simply `len(pattern)`.

    Pre: a string > substring.

    Post: returns a list of indices where the substring was found.

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
    bmbc = [pattern_length] * 256
    for index, char in enumerate(pattern[:-1]):
        bmbc[ord(char)] = pattern_length - index - 1
    bmbc = tuple(bmbc)
    search_index = pattern_length - 1
    while search_index < text_length:
        pattern_index = pattern_length - 1
        text_index = search_index
        while text_index >= 0 and \
              text[text_index] == pattern[pattern_index]:
            pattern_index -= 1
            text_index -= 1
        if pattern_index == -1:
            offsets.append(text_index + 1)
        search_index += bmbc[ord(text[search_index])]

    return offsets
