"""
    Pollard Rho Algorithm
    ---------------------
    Pollard's rho algorithm is a special-purpose integer factorization
    algorithm. It was invented by John Pollard in 1975. It is particularly
    effective for a composite number having a small prime factor.

"""
import random

from algorithms.math.primality_test import is_prime
from fractions import gcd


def f(x):
    """
    """
    return x*x+1


def rho(n, x1=2, x2=2):
    """
    """
    if n % 2 == 0:
        return 2
    i = 0
    while True:
        x1 = f(x1) % n
        x2 = f(f(x2)) % n
        divisor = gcd(abs(x1-x2), n)
        i += 1
        if(divisor != 1):
            break
        if i > 500:
            x1 = random.randint(1, 10)
            x2 = random.randint(1, 10)
            i = 0
    return divisor


def pollard_rho_rec(x, factors):
    """
    """
    if x == 1:
        return

    if is_prime(x):
        factors.append(x)
        return

    divisor = rho(int(x), random.randint(1, 10), random.randint(1, 10))
    pollard_rho_rec(int(divisor), factors)
    pollard_rho_rec(int(x/divisor), factors)


def pollard_rho(x):
    """
    """
    if x == 1 or x == 0:
        return [x]
    factors = []
    pollard_rho_rec(x, factors)
    return factors
