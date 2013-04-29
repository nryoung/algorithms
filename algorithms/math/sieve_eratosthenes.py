"""
    sieve_eratosthenes.py

    Implementation of the Sieve of Eratosthenes algorithm.

    Sieve of Eratosthenes Overview:
    ------------------------
    Is a simple, ancient algorithm for finding all prime numbers 
    up to any given limit. It does so by iteratively marking as composite (i.e. not prime) 
    the multiples of each prime, starting with the multiples of 2.

    The sieve of Eratosthenes is one of the most efficient ways 
    to find all of the smaller primes (below 10 million or so).

    Time Complexity: O(n log log n)

    Pseudocode: https://en.wikipedia.org/wiki/Sieve_of_Eratosthenes    
"""

def eratosthenes(end,start=2):
    if start < 2:
        start = 2
    primes = range(start,end)
    marker = 2
    while marker < end:
        for i in xrange(marker, end+1):
            if marker*i in primes:
                primes.remove(marker*i)
        marker += 1
    return primes
        
    
