""" Implementation of Quick Sort """
import random

def sort(seq):
   
   if len(seq) < 1:
       return seq
   else:
       pivot = seq[0]
       left = sort([x for x in seq[1:] if x < pivot])
       right = sort([x for x in seq[1:] if x >= pivot])
       return left + [pivot] + right

if __name__ == '__main__':
    seq = range(10)
    random.shuffle(seq)
    print "Not Sorted!"
    for x in seq:
        print x

    new_seq = sort(seq)
    print "Sorted!"
    for n in new_seq:
        print n
