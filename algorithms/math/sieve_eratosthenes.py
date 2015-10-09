"""
    Sieve of Eratosthenes
    ---------------------
    Is a simple, ancient algorithm for finding all prime numbers
    up to any given limit. It does so by iteratively marking as composite
    (i.e. not prime) the multiples of each prime, starting with the multiples
    of 2.

    The sieve of Eratosthenes is one of the most efficient ways
    to find all of the smaller primes (below 10 million or so).

    Time Complexity: O(n log log n)

    Pseudocode: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes
"""


def eratosthenes(end, start=2, return_boolean=False):
    """
    Finds all primes < `end`.

    :param end: An integer. The upper limit of the range to look for primes.
    :param start: An integer. The start of the range to look for primes.
    :param return_boolean: A boolean. Represents the type of return type.
    :rtype: Depending on `return_boolean` either returns boolean and primes or
            just the primes.
    """
    primes = []
    if end < start or end < 2:
        return []
    is_prime = [True for i in range(end + 1)]
    is_prime[0] = is_prime[1] = False
    for i in range(2, end + 1):
        if not is_prime[i]:
            continue
        if start <= i <= end:
            primes.append(i)
        j = i * i
        while j <= end:
            is_prime[j] = False
            j += i
    if return_boolean:
        return primes, is_prime
    return primes
