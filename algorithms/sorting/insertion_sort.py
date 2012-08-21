""" Implementation of Insertion Sort """

def sort(seq):
    for n in range(1, len(seq)):
        item = seq[n]
        hole = n
        while hole > 0 and seq[ hole - 1] > item:
            seq[hole] = seq[hole - 1]
            hole = hole - 1
        seq[hole] = item
    return seq
