""" Implementation of KMP search """

def search(string, word):
    n = len(string)
    m = len(word)
    pi = compute_prefix(word)
    q = 0
    for i in range(n):
        while q > 0 and word[q] != string[i]:
            q = pi[q - 1]
        if word[q] == string[i]:
            q = q + 1
        if q == m:
            return i - m + 1
    return False

def compute_prefix(word):
    m = len(word)
    pi = [0] * m
    k = 0

    for q in range(1, m):
        while k > 0 and word[k] != word[q]:
            k = pi[k - 1]
        
        if word[k + 1] == word[q]:
            k = k + 1
        pi[q] = k
    return pi
