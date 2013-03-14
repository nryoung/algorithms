import unittest
from ..math.extended_gcd import extended_gcd
from ..math.lcm import lcm


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
        # Find lcm of 16 and 20
        r = lcm(16, 20)
        self.assertEqual(80, abs(r))

        # Find lcm for 20 and 16
        r2 = lcm(20, 16)

        # Checks that lcm function is commutative
        self.assertEqual(r, r2)
