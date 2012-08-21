""" Implementation of Bubble Sort. """

def sort(seq):

    for x in seq:
        temp = 0
        for n in range(1, len(seq)):
            temp = seq[n]
            if seq[n] < seq[n-1]:
                seq[n] = seq[n-1]
                seq[n-1] = temp
    return seq    
