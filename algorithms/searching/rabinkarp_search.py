"""
    rabinkarp_search.py

    Implementation of Rabin-Karp search on a given string.

    Rabin-Karp Search Overview:
    ------------------------
    Search for a substring in a given string, by comparing hash values
    of the strings.

    Time Complexity: O(nm)

    Psuedo Code: http://en.wikipedia.org/wiki/Rabin-Karp_algorithm

"""

from hashlib import md5


def search(s, sub):
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
