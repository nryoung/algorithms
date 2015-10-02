from math import sqrt

"""
    fermat.py

    Implementation of the Fermat factorization.

    Fermat factorization Overview:
    ------------------------
    Fermat's factorization method is based on the representation
    of an odd integer as the difference of two squares:
    N = a*a-b*b = (a-b)*(a+b)

"""


def fermat(n):
    if n & 1 == 0:
        return [n >> 1, 2]
    x = int(sqrt(n))
    if x*x == n:
        return [x, x]
    x += 1
    while True:
        y2 = x*x-n
        y = int(sqrt(y2))
        if y*y == y2:
            break
        else:
            x += 1
    return [x-y, x+y]
