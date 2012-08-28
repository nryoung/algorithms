""" Implementation of Heap Sort """

def parent(i):
    return i/2

def left(i):
    return 2*i

def right(i):
    return 2*i+1

def max_heapify(seq, i, n):
    l = left(i)
    r = right(i)

    if l <= n and seq[n] > seq[i]:
        largest = l
    else:
        largest = i
    if r <= n and seq[r] > seq[largest]:
        largest = r
    
    if largest != i:
        seq[i], seq[largest] = seq[largest], seq[i]
        max_heapify(seq, largest, n)

def heap_length(seq):
    return len(seq) - 1

def build_heap(seq):
    n = heap_length(seq)
    for i in range(n/2,0,-1):
        max_heapify(seq, i, n)

def sort(seq):
    build_heap(seq)
    heap_size = heap_length(seq)
    for i in range(heap_size,1,-1):
        seq[1], seq[i] = seq[i], seq[1]
        heap_size = heap_size - 1
        max_heapify(seq, 1, heap_size)
    
    return seq
