"""
    Approximate Cumulative Distribution Function
    --------------------------------------------
    Calculates the cumulative distribution function (CDF)
    of the normal distribution based on an approximation by George Marsaglia:
    Marsaglia, George (2004). "Evaluating the Normal Distribution".
    Journal of Statistical Software 11 (4).

    16 digit precision for 300 iterations when x = 10.

    Equation:


    f(x) = 1/2 + pdf(x) * (x + (x^3/3) + (x^5/3*5) + (x^7/3*7) + ...)
"""

from algorithms.math import std_normal_pdf


def cdf(x, iterations=300):
    """
    Calculates the cumulative distribution function of the normal distribution.
    Uses a taylor exponent to calculate this.

    :param x: An integer that represents the taylor exponent.
    :param iterations: An integer representing the number of iterations.
    :rtype: The normal distribution
    """
    product = 1.0
    taylor_exp = [x]
    for i in range(3, iterations, 2):
        product *= i
        taylor_exp.append(float(x**i)/product)
    taylor_fact = sum(taylor_exp)

    return (0.5 + (taylor_fact * std_normal_pdf.pdf(x, mean=0, std_dev=1)))
