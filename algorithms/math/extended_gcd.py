"""
    Extended Greatest Common Divisor
    --------------------------------
    Implementation of the extended greatest common divisor algorithm.

    Pseudo Code: http://en.wikipedia.org/wiki/Extended_Euclidean_algorithm
"""


def extended_gcd(p, q):
    """
    Find the greatest common divisor and returns them.

    :param a: An integer.
    :param b: An integer.
    :rtype: A tuple representing the greatest common divisor.
    """
    (a, b) = (p, q)

    if a < 0:
        a = -1 * a

    if b < 0:
        b = -1 * b

    x0 = 0
    y1 = 0

    x1 = 1
    y0 = 1

    while(b != 0):
        quotient = a // b
        (a, b) = (b, a % b)
        (x1, x0) = (x0 - quotient * x1, x1)
        (y1, y0) = (y0 - quotient * y1, y1)

    if p < 0:
        y0 = -1 * y0

    if q < 0:
        x0 = -1 * x0

    return (y0, x0)
