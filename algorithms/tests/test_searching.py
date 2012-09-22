""" Unit Tests for searching """
import unittest
from ..searching import binary_search, kmp_search

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
        self.assertIs(rv1, 0)
        self.assertIs(rv2, 0)
        self.assertFalse(rv3)
        self.assertFalse(rv4)

class TestKMPSearch(unittest.TestCase):
    """
    Tests KMP search on string "ABCDE FG ABCDEABCDEF"
    """
    def test_kmpsearch(self):
        self.string = "ABCDE FG ABCDEABCDEF"
        rv1 = kmp_search.search(self.string, "ABCDEA")
        rv2 = kmp_search.search(self.string, "ABCDER")
        self.assertIs(rv1, 9)
        self.assertFalse(rv2)
