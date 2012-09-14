""" Implementation of Binary Search """

def search(seq, key):
    imin = 0
    imax = len(seq) - 1
    
    if imax < imin :
        return False

    else:
        mid = len(seq) / 2

        if seq[mid] > key:
            return search(seq[:mid-1], key)

        elif seq[mid] < key:
            return search(seq[mid+1:], key)

        else:
            return True
