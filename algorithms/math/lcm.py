def lcm(a, b):
    """
    Simple version of lcm, that does not have any dependencies
    """
    tmp_a = a
    while (tmp_a % b) != 0:
        tmp_a += a
    return tmp_a
