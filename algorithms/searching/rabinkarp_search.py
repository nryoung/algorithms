"""
    rabinkarp_search.py

    This module implements Rabin-Karp search on a given string.

    Rabin-Karp Search Overview:
    ------------------------
    Search for a substring in a given string, by comparing hash values of the strings.

    Pre: two strings, one to search in and one to search for.

    Post: returns the index of the start of the search string.

    Time Complexity:  O(nm)

    Psuedo Code: http://en.wikipedia.org/wiki/Rabin-Karp_algorithm

    rabinkarp_search.search(searchString, targetString) -> integer
    rabinkarp_search.search(searchString, targetString) -> False
"""

import hashlib

def search(s,sub):
	n, m = len(s), len(sub)
	hsub, hs = hashlib.md5(sub), hashlib.md5(s[0:m])

	for i in range(n - m + 1):
		if hs.hexdigest() == hsub.hexdigest():
			if s[i:i+m] == sub:
				return i
		news = s[i+1:i+m+1]
		hs = hashlib.md5(news)

	return False