"""
    Sieve of Atkin
    --------------
    It is an optimized version of the ancient sieve of Eratosthenes
    which does some preliminary work and then marks off
    multiples of the square of each prime, rather than multiples of the prime
    itself. It was created in 2004 by A. O. L. Atkin and Daniel J. Bernstein.

    Time Complexity: O(n/log log n)

    Pseudocode: https://en.wikipedia.org/wiki/Sieve_of_Atkin
"""
from math import sqrt


def atkin(limit):
    """
    :param limit: The upper limit in which to find all primes less than this
                  value.
    """
    if limit == 2:
        return [2]
    if limit == 3:
        return [2, 3]
    if limit == 5:
        return [2, 3, 5]
    if limit < 2:
        return []
    primes = [2, 3, 5]
    is_prime = [False] * (limit + 1)
    sqrt_limit = int(sqrt(limit)) + 1

    for x in range(1, sqrt_limit):
        for y in range(1, sqrt_limit):
            n = 4 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 1 or n % 12 == 5):
                is_prime[n] = not is_prime[n]
            n = 3 * x ** 2 + y ** 2
            if n <= limit and (n % 12 == 7):
                is_prime[n] = not is_prime[n]
            n = 3 * x ** 2 - y ** 2
            if x > y and (n <= limit) and (n % 12 == 11):
                is_prime[n] = not is_prime[n]

    for index in range(5, sqrt_limit):
        if is_prime[index]:
            for composite in range(index ** 2, limit, index ** 2):
                is_prime[composite] = False
    for index in range(7, limit):
        if is_prime[index]:
            primes.append(index)
    return primes
