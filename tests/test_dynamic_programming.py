import unittest

from algorithms.dynamic_programming.lcs import lcs


class TestLCS(unittest.TestCase):
    """
    Tests the Longest Common Subsequence of several strings
    """

    def test_lcs(self):
        str1 = "BANANA"
        str2 = "ABA"
        str3 = "BCAD"
        str4 = "NNAD"

        self.assertEqual(lcs(str1, str1), str1)
        self.assertEqual(lcs(str1, str2), "BA")
        self.assertEqual(lcs(str1, str3), "BA")
        self.assertEqual(lcs(str1, str4), "NNA")
        self.assertEqual(lcs(str2, str3), "BA")
        self.assertEqual(lcs(str2, str4), "A")
        self.assertEqual(lcs(str3, str4), "AD")
