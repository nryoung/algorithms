"""
    Trial Division
    --------------
    Trial division is the most laborious but easiest
    to understand of the integer factorization algorithms.
    Try to divide a number n by all prime numbers < sqrt(n).

"""
from algorithms.math.sieve_eratosthenes import eratosthenes


def trial_division(n):
    """
    Uses trial division to find prime factors of `n`.

    :param n: An integer to factor.
    :rtype: The prime factors of `n`
    """
    prime_factors = []
    if n < 2:
        return prime_factors
    for p in eratosthenes(int(n**0.5) + 1):
        if p*p > n:
            break
        while n % p == 0:
            prime_factors.append(p)
            n //= p
    if n > 1:
        prime_factors.append(n)
    return prime_factors
