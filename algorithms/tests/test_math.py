import unittest
from ..math.extended_gcd import extended_gcd
from ..math.lcm import lcm
from ..math.sieve_eratosthenes import eratosthenes


class TestExtendedGCD(unittest.TestCase):

    def test_extended_gcd(self):
        # Find extended_gcd of 35 and 77
        (a, b) = extended_gcd(35, 77)
        self.assertIs(35 * a + 77 * b, 7)

        # Find extended_gcd of 15 and 19
        (a, b) = extended_gcd(15, 19)
        self.assertIs(15 * a + 19 * b, 1)

        # Find extended_gcd of 18 and 9
        (a, b) = extended_gcd(18, 9)
        self.assertIs(18 * a + 9 * b, 9)

        # Find extended_gcd of 99 and 81
        (a, b) = extended_gcd(99, 81)
        self.assertIs(99 * a + 81 * b, 9)

        # Find extended_gcd of 50 and 15
        (a, b) = extended_gcd(50, 15)
        self.assertIs(50 * a + 15 * b, 5)


class TestLCM(unittest.TestCase):
    def test_lcm(self):
        # Find lcm of (16, 20) and (20, 16)
        r, r2 = lcm(16, 20), lcm(20, 16)
        self.assertEqual(r, 80)

        # Checks that lcm function is commutative
        self.assertEqual(r, r2)


class TestSieveOfEratosthenes(unittest.TestCase):

    def test_eratosthenes(self):
        rv1 = eratosthenes(-10)
        rv2 = eratosthenes(10)
        rv3 = eratosthenes(100,5)
        rv4 = eratosthenes(100,-10)
        self.assertEqual(rv1,[])
        self.assertEqual(rv2,[2, 3, 5, 7])
        self.assertEqual(rv3,[5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
        self.assertEqual(rv4,[2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97])
