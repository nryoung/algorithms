from extended_gcd import extended_gcd


def lcm(a, b):
    """
    Returns LCM based on GCD of digit.
    """
    x, y = extended_gcd(a, b)
    return a * b / (a * y + b * x)
