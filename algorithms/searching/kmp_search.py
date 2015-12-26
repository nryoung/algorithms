"""

    KMP Search
    ----------
    Implementation of kmp search on string. Uses a prefix function to reduce
    the searching time.

    Time Complexity:  O(n + k), where k is the substring to be found

    Psuedo Code: CLRS. Introduction to Algorithms. 3rd ed.

"""


def search(string, word):
    """
    Searches for occurrences of a "word" within a main "string" by employing
    the observation that when a mismatch occurs, the word itself embodies
    sufficient information to determine where the next match could begin,
    thus bypassing re-examination of previously matched characters.

    :param string: The string to be searched.
    :param word: The sub string to be searched for.
    :rtype: The indices of all occurences of where the substring is found in
            the string.
    """
    word_length = len(word)
    string_length = len(string)
    offsets = []

    if word_length > string_length:
        return offsets

    prefix = compute_prefix(word)
    q = 0
    for index, letter in enumerate(string):
        while q > 0 and word[q] != letter:
            q = prefix[q - 1]
        if word[q] == letter:
            q += 1
        if q == word_length:
            offsets.append(index - word_length + 1)
            q = prefix[q - 1]
    return offsets


def compute_prefix(word):
    """
    Returns the prefix of the word.

    :param word: The sub string that the prefix will be computed for.
    :rtype: Returns computed prefix of the word.
    """
    word_length = len(word)
    prefix = [0] * word_length
    k = 0

    for q in range(1, word_length):
        while k > 0 and word[k] != word[q]:
            k = prefix[k - 1]

        if word[k + 1] == word[q]:
            k = k + 1
        prefix[q] = k
    return prefix
