""" Unit Tests for searching """
import unittest
from ..searching import binary_search, kmp_search, rabinkarp_search, bmh_search


class TestBinarySearch(unittest.TestCase):
    """
    Tests Binary Search on a small range from 0-9
    """

    def test_binarysearch(self):
        self.seq = range(10)
        rv1 = binary_search.search(self.seq, 0)
        rv2 = binary_search.search(self.seq, 9)
        rv3 = binary_search.search(self.seq, -1)
        rv4 = binary_search.search(self.seq, 10)
        rv5 = binary_search.search(self.seq, 4)
        self.assertIs(rv1, 0)
        self.assertIs(rv2, 9)
        self.assertFalse(rv3)
        self.assertFalse(rv4)
        self.assertIs(rv5, 4)
        self.seq = range(9)
        rv1 = binary_search.search(self.seq, 0)
        rv2 = binary_search.search(self.seq, 8)
        rv3 = binary_search.search(self.seq, -1)
        rv4 = binary_search.search(self.seq, 10)
        rv5 = binary_search.search(self.seq, 4)
        self.assertIs(rv1, 0)
        self.assertIs(rv2, 8)
        self.assertFalse(rv3)
        self.assertFalse(rv4)
        self.assertIs(rv5, 4)

class TestKMPSearch(unittest.TestCase):
    """
    Tests KMP search on string "ABCDE FG ABCDEABCDEF"
    """

    def test_kmpsearch(self):
        self.string = "ABCDE FG ABCDEABCDEF"
        rv1 = kmp_search.search(self.string, "ABCDEA")
        rv2 = kmp_search.search(self.string, "ABCDER")
        self.assertIs(rv1[0], 9)
        self.assertFalse(rv2)


class TestRabinKarpSearch(unittest.TestCase):
    """
    Tests Rabin-Karp search on string "ABCDEFGHIJKLMNOP"
    """

    def test_rabinkarpsearch(self):
        self.string = "ABCDEFGHIJKLMNOP"
        rv1 = rabinkarp_search.search(self.string, "MNOP")
        rv2 = rabinkarp_search.search(self.string, "BCA")
        self.assertIs(rv1[0], 12)
        self.assertFalse(rv2)


class TestBMHSearch(unittest.TestCase):
    """
    Tests BMH search on string "ABCDE FG ABCDEABCDEF"
    """

    def test_bmhsearch(self):
        self.string = "ABCDE FG ABCDEABCDEF"
        rv1 = bmh_search.search(self.string, "ABCDEA")
        rv2 = bmh_search.search(self.string, "ABCDER")
        self.assertIs(rv1[0], 9)
        self.assertFalse(rv2)
