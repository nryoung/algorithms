import random
import unittest
from ..sorting import bubble_sort, selection_sort, insertion_sort, merge_sort, quick_sort, heap_sort, shell_sort, comb_sort

class TestBubbleSort(unittest.TestCase):
    """
    Tests Bubble sort on a small range from 0-9
    """
    def test_bubblesort(self):
        self.seq = range(10)
        random.shuffle(self.seq)
        rv = bubble_sort.sort(self.seq)
        self.assertIs(self.seq[0], 0)
        self.assertIs(self.seq[-1], 9)

class TestSelectionSort(unittest.TestCase):
    """
    Tests Selection sort on a small range from 0-9
    """
    def test_selectionsort(self):
        self.seq = range(10)
        random.shuffle(self.seq)
        rv = selection_sort.sort(self.seq)
        self.assertIs(self.seq[0], 0)
        self.assertIs(self.seq[-1], 9)

class TestInsertionSort(unittest.TestCase):
    """
    Tests Insertion sort on a small range from 0-9
    """
    def test_selectionsort(self):
        self.seq = range(10)
        random.shuffle(self.seq)
        rv = insertion_sort.sort(self.seq)
        self.assertIs(self.seq[0], 0)
        self.assertIs(self.seq[-1], 9)

class TestMergeSort(unittest.TestCase):
    """
    Tests Merge sort on a small range from 0-9
    also tests merge function included in merge sort
    """
    def test_mergesort(self):
        self.seq = range(10)
        random.shuffle(self.seq)
        self.seq = merge_sort.sort(self.seq)
        self.assertIs(self.seq[0], 0)
        self.assertIs(self.seq[-1], 9)

    def test_merge(self):
        self.seq1 = range(5)
        self.seq2 = range(5,10)
        self.seq = merge_sort.merge(self.seq1, self.seq2)
        self.assertIs(self.seq[0], 0)
        self.assertIs(self.seq[-1], 9)

class TestQuickSort(unittest.TestCase):
    """
    Test Quick sort on a small range from 0-9
    """

    def test_quicksort(self):
        self.seq = range(10)
        random.shuffle(self.seq)
        self.seq = quick_sort.sort(self.seq)
        self.assertIs(self.seq[0], 0)
        self.assertIs(self.seq[-1], 9)

class TestHeapSort(unittest.TestCase):
    """
    Test Heap sort on a small range from 0-9
    """

    def test_heapsort(self):
        self.seq = range(10)
        random.shuffle(self.seq)
        self.seq = heap_sort.sort(self.seq)
        self.assertIs(self.seq[0], 0)
        self.assertIs(self.seq[-1], 9)

class TestShellSort(unittest.TestCase):
    """
    Test Shell sort on a small range from 0-9
    """

    def test_shellsort(self):
        self.seq = range(10)
        random.shuffle(self.seq)
        self.seq = shell_sort.sort(self.seq)
        self.assertIs(self.seq[0], 0)
        self.assertIs(self.seq[-1], 9)

class TestCombSort(unittest.TestCase):
    """
    Test Comb sort on a small range from 0-9
    """

    def test_combsort(self):
        self.seq = range(10)
        random.shuffle(self.seq)
        self.seq = comb_sort.sort(self.seq)
        self.assertIs(self.seq[0], 0)
        self.assertIs(self.seq[-1], 9)
