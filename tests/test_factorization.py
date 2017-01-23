import random
import unittest

from algorithms.factorization.pollard_rho import pollard_rho
from algorithms.factorization.trial_division import trial_division
from algorithms.factorization.fermat import fermat


class TestFermat(unittest.TestCase):

    def test_fermat(self):
        x = random.randint(1, 100000000)
        factors = fermat(x)
        res = 1
        for i in factors:
            res *= i
        self.assertEqual(x, res)


class TestPollardRho(unittest.TestCase):

    def test_pollard_rho(self):
        x = random.randint(1, 100000000000)
        factors = pollard_rho(x)
        res = 1
        for j in factors:
            res *= j
        self.assertEqual(x, res)

    def test_pollard_rho_x_is_zero(self):
        x = 0
        factors = pollard_rho(x)
        res = 1
        for j in factors:
            res *= j
        self.assertEqual(x, res)


class TestTrialDivision(unittest.TestCase):

    def test_trial_division(self):
        x = random.randint(0, 10000000000)
        factors = trial_division(x)
        res = 1
        for i in factors:
            res *= i
        self.assertEqual(x, res)
