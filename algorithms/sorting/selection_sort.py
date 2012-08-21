""" Implementation of Selection Sort. """

def sort(seq):
  
    for i in range(0, len(seq)):
        minat = i
        minum = seq[i]
        for j in range(i+1, len(seq)):
            if minum > seq[j]:
                minat = j
                minum = seq[j]
        temp = seq[i]
        seq[i] = seq[minat]
        seq[minat] = temp

    return seq
