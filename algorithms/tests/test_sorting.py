import random
import unittest
from ..sorting import bubble_sort, selection_sort, insertion_sort

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
