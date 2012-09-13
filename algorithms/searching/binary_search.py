""" Implementation of Binary Search """

def search(seq, key):
    
    if len(seq) == 0:
        return False

    else:
        mid = len(seq)/2

        if seq[mid] > key:
            return search(seq[:mid], key)

        elif seq[mid] < key:
            return search(seq[mid:], key)

        else:
            return True
