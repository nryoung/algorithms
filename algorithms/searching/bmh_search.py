"""
    BMH Search
    ----------
    Search that attempts to find a substring in a string. Uses a bad-character
    shift of the rightmost character of the window to compute shifts.

    Time: Complexity: O(m + n), where m is the substring to be found.

    Space: Complexity: O(m), where m is the substring to be found.

    Psuedo Code: https://github.com/FooBarWidget/boyer-moore-horspool

"""


def search(text, pattern):
    """
    Takes a string and searches if the `pattern` is substring within `text`.

    :param text: A string that will be searched.
    :param pattern: A string that will be searched as a substring within
                    `text`.
    :rtype: The indices of all occurences of where the substring `pattern`
            was found in `text`.
    """

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
