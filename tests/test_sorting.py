import random
import unittest

from algorithms.sorting import (
    bogo_sort,
    bubble_sort,
    cocktail_sort,
    comb_sort,
    gnome_sort,
    heap_sort,
    insertion_sort,
    merge_sort,
    quick_sort,
    quick_sort_in_place,
    selection_sort,
    shell_sort,
    strand_sort,
)


class SortingAlgorithmTestCase(unittest.TestCase):
    """
    Shared code for a sorting unit test.
    """

    def setUp(self):
        self.input = list(range(10))
        random.shuffle(self.input)
        self.correct = list(range(10))


class TestBogoSort(SortingAlgorithmTestCase):
    """
    Tests Bogo sort on a small range from 0-9
    """

    def test_bogosort(self):
        self.output = bogo_sort.sort(self.input)
        self.assertEqual(self.correct, self.input)


class TestBubbleSort(SortingAlgorithmTestCase):
    """
    Tests Bubble sort on a small range from 0-9
    """

    def test_bubblesort(self):
        self.output = bubble_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)


class TestCocktailSort(SortingAlgorithmTestCase):
    """
    Tests Cocktail sort on a small range from 0-9
    """

    def test_cocktailsort(self):
        self.output = cocktail_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)


class TestCombSort(SortingAlgorithmTestCase):
    """
    Tests Comb sort on a small range from 0-9
    """

    def test_combsort(self):
        self.output = comb_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)


class TestGnomeSort(SortingAlgorithmTestCase):
    """
    Tests Gnome sort on a small range from 0-9
    """

    def test_gnomesort(self):
        self.output = gnome_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)


class TestHeapSort(SortingAlgorithmTestCase):
    """
    Test Heap sort on a small range from 0-9
    """

    def test_heapsort(self):
        self.output = heap_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)


class TestInsertionSort(SortingAlgorithmTestCase):
    """
    Tests Insertion sort on a small range from 0-9
    """

    def test_insertionsort(self):
        self.output = insertion_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)


class TestMergeSort(SortingAlgorithmTestCase):
    """
    Tests Merge sort on a small range from 0-9
    also tests merge function included in merge sort
    """

    def test_mergesort(self):
        self.output = merge_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)

    def test_merge(self):
        self.seq1 = list(range(0, 5))
        self.seq2 = list(range(5, 10))
        self.seq = merge_sort.merge(self.seq1, self.seq2)
        self.assertIs(self.seq[0], 0)
        self.assertIs(self.seq[-1], 9)


class TestQuickSort(SortingAlgorithmTestCase):
    """
    Test Quick sort on a small range from 0-9
    """

    def test_quicksort(self):
        self.output = quick_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)


class TestQuickSortInPlace(SortingAlgorithmTestCase):
    """
    Tests Quick sort in place version on a small range from 0-9
    also tests partition function included in quick sort
    """
    def test_quicksort_in_place(self):
        self.output = quick_sort_in_place.sort(
            self.input, 0,
            len(self.input)-1
        )
        self.assertEqual(self.correct, self.output)

    def test_partition(self):
        self.seq = list(range(10))
        self.assertIs(
            quick_sort_in_place.partition(
                self.seq, 0,
                len(self.seq)-1, 5),
            5
        )


class TestSelectionort(SortingAlgorithmTestCase):
    """
    Test Selection sort on a small range from 0-9
    """

    def test_selectionsort(self):
        self.output = selection_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)


class TestShellSort(SortingAlgorithmTestCase):
    """
    Test Shell sort on a small range from 0-9
    """

    def test_shellsort(self):
        self.output = shell_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)


class TestStrandSort(SortingAlgorithmTestCase):
    """
    Tests Strand sort on a small range from 0-9
    """

    def test_strandsort(self):
        self.output = strand_sort.sort(self.input)
        self.assertEqual(self.correct, self.output)
