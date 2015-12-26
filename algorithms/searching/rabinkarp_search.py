"""
    Implementation of Rabin-Karp search on a given string.

    Rabin-Karp Search
    -----------------
    Search for a substring in a given string, by comparing hash values
    of the strings.

    Time Complexity: O(nm)

    Psuedo Code: http://en.wikipedia.org/wiki/Rabin-Karp_algorithm

"""

from hashlib import md5


def search(s, sub):
    """
    Uses hashing to find any one of a set of pattern strings in a text.

    :param s: The string to be searched.
    :param sub: The substring to be searched for.
    :rtype: The indices of all occurences of where the substring is found in
            the string.
    """
    n, m = len(s), len(sub)
    hsub_digest = md5(sub.encode('utf-8')).digest()
    offsets = []
    if m > n:
        return offsets

    for i in range(n - m + 1):
        if md5(s[i:i + m].encode('utf-8')).digest() == hsub_digest:
            if s[i:i + m] == sub:
                offsets.append(i)

    return offsets
