from math import sqrt

from algorithms.math.sieve_eratosthenes import eratosthenes


CACHE_LIMIT = 10 ** 6
primes_cache_list = []
primes_cache_bool = []


def is_prime(number, cache=True):
    if number < 2:
        return False
    global primes_cache_list, primes_cache_bool
    if cache and len(primes_cache_list) == 0:
        primes_cache_list, primes_cache_bool = eratosthenes(
            CACHE_LIMIT, return_boolean=True
        )
        for prime in primes_cache_list:
            primes_cache_bool[prime] = True
    if number < len(primes_cache_bool):
        return primes_cache_bool[number]

    sqrt_number = sqrt(number)
    for prime in primes_cache_list:
        if prime > sqrt_number:
            return True
        if number % prime == 0:
            return False

    to_check = 2
    if len(primes_cache_list) > 0:
        to_check = primes_cache_list[-1] + 1
    while to_check <= sqrt_number:
        if number % to_check == 0:
            return False
        to_check += 1
    return True
