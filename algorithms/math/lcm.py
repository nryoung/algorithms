"""
    Lowest Common Multiple
    ----------------------
    Simple implementation of the Lowest Common Multiple Algorithm.

    Pseudo Code: https://en.wikipedia.org/wiki/Least_common_multiple
"""


def lcm(a, b):
    """
    Simple version of lcm, that does not have any dependencies.

    :param a: Integer
    :param b: Integer
    :rtype: The lowest common multiple of integers a and b
    """
    tmp_a = a
    while (tmp_a % b) != 0:
        tmp_a += a
    return tmp_a
