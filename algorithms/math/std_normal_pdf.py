"""
    Calculates the normal distribution's probability density
    function (PDF).
    Calculates Standard normal pdf for mean=0, std_dev=1.

    Equation:
    f(x) = 1 / sqrt(2*pi) * e^(-(x-mean)^2/ 2*std_dev^2)
"""


def pdf(x, mean=0, std_dev=1):

    PI = 3.141592653589793
    E = 2.718281828459045
    term1 = 1.0 / ((2 * PI)**0.5)
    term2 = E**(-1.0*(x-mean)**2.0 / 2.0*(std_dev**2.0))

    return term1 * term2
