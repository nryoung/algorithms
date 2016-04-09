import unittest

from algorithms.shuffling import knuth


class ShufflingAlgorithmTestCase(unittest.TestCase):
    """
    Shared code for shuffling unit tests.
    """

    def setUp(self):
        self.sorted = range(10)


class TestKnuthShuffle(ShufflingAlgorithmTestCase):
    """
    Tests Knuth shuffle on a small range from 0-9
    """
    def test_knuthshuffle(self):
        self.shuffle = knuth.shuffle(list(range(10)))
        self.not_shuffled = 0

        for i in self.sorted:
            if i == self.shuffle[i]:
                self.not_shuffled += 1

        self.assertGreater(5, self.not_shuffled)
