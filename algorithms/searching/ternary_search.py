"""
    Ternary search
    ---------------
    Finds the maximum of unimodal function fn() within [left, right]
    To find the minimum, revert the if/else statement or revert the comparison.

    Time Complexity: O(log(n))

"""


def search(fn, left, right, precision):
    while abs(right - left) > precision:
        left_third = left + (right - left) / 3
        right_third = right - (right - left) / 3

        if fn(left_third) < fn(right_third):
            left = left_third
        else:
            right = right_third

    return (left + right) / 2
