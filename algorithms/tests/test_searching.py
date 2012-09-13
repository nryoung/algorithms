""" Unit Tests for searching """
import unittest
from ..searching import binary_search

class TestBinarySearch(unittest.TestCase):
    """
    Tests Binary Search on a small range from 0-9
    """
    def test_binarysearch(self):
        self.seq = range(10)
        rv1 = binary_search.search(self.seq, 8)
        rv2 = binary_search.search(self.seq, 3)
        self.assertTrue(rv1)
        self.assertTrue(rv2)
