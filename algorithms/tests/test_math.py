import unittest
import nose

from ..math.extended_gcd import extended_gcd
from ..math.std_normal_pdf import pdf
from ..math.approx_cdf import cdf

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


class TestStdNormPDF(unittest.TestCase):

    def test_pdf(self):
        # Calculate standard normal pdf for x=1
        a = pdf(1)
        nose.tools.assert_almost_equal(a, 0.24197072451914337)

        # Calculate standard normal pdf for x=(-1)
        a = pdf(-1)
        nose.tools.assert_almost_equal(a, 0.24197072451914337)

        # Calculate standard normal pdf for x=13, mean=10, std_dev=1
        a = pdf(x=13, mean=10, std_dev=1)
        nose.tools.assert_almost_equal(a, 0.004431848411938008)


class TestApproxCdf(unittest.TestCase):

    def test_cdf(self):
        # Calculate cumulative distribution function for x=1
        a = cdf(1)
        nose.tools.assert_almost_equal(a, 0.841344746068543)

        # Calculate cumulative distribution function x=0
        a = cdf(0)
        nose.tools.assert_almost_equal(a, 0.5)

        # Calculate cumulative distribution function for x=(-1)
        a = cdf(-1)
        nose.tools.assert_almost_equal(a, 0.15865525393145702)

