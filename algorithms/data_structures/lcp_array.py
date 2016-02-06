import math

"""
    Suffix Array
    ------------------
    In computer science, a suffix array is a sorted array of all suffixes
    of a string. It is a data structure used, among others, in full text
    indices, data compression algorithms and  within the field
    of bioinformatics.

    for more info : http://algs4.cs.princeton.edu/63suffix/
    Complexity :
        worst case : O(n log(n))
"""


def suffix_array(t):
    """
    Suffix array of a string t
    :param t: the string to extract suffix array from
    :return (s_array, rank): return a tuple that contain the  suffix array
    and the rank array which is the reversed version of the suffix array
    """
    length = len(t)
    rank = [0] * length
    s_array = [0] * length
    tuple_array = [0] * length
    iterations = int(math.log(length, 2)) + 1
    size = 1

    for i, t in enumerate(t):
        s_array[i] = ord(t)

    for _ in range(iterations):
        for i, ele in enumerate(tuple_array):
            if i + size < length:
                tuple_array[i] = ((s_array[i], s_array[i + size]), i)
            else:
                tuple_array[i] = ((s_array[i], -1), i)
        tuple_array.sort()
        s_array[tuple_array[0][1]] = 0
        for i in range(1, len(tuple_array)):
            cls, idx = tuple_array[i]
            if cls == tuple_array[i - 1][0]:
                s_array[idx] = s_array[tuple_array[i - 1][1]]
            else:
                s_array[idx] = s_array[tuple_array[i - 1][1]] + 1
        size *= 2

    for i, p in enumerate(s_array):
        rank[p] = i

    return s_array, rank


"""
    LCP Array
    ------------------
    the longest common prefix array (LCP array) is an auxiliary data
    structure to the suffix array. It stores the lengths of the longest
    common prefixes (LCPs) between all pairs of consecutive suffixes
    in a sorted suffix array.

    I use Kasai's algorithm in implementation :
    Pseudo Code: http://algs4.cs.princeton.edu/32bst

    Complexity :
     worst case :O(n)

"""


def lcp_array(t_str, s_array, rank):
    """

    :param t_str: the string to calculate the lcp array for
    :param s_array: the suffix array of the string
    :param rank: the suffix array reversed
    :return: the lcp array
    """
    t_length = len(t_str)
    lcp = [0] * t_length
    last_lcp = 1

    for i, ele in enumerate(s_array):
        last_lcp = last_lcp - 1 if last_lcp > 1 else 0
        if ele == t_length - 1:
            last_lcp = 0
            lcp[ele] = last_lcp
            continue
        n_suffix = rank[ele + 1]

        while i + last_lcp < t_length \
                and n_suffix + last_lcp < t_length \
                and t_str[i + last_lcp] == t_str[n_suffix + last_lcp]:
            last_lcp += 1
        lcp[ele] = last_lcp

    return lcp
