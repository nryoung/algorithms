""" Unit Tests for searching """
import unittest
import math

from algorithms.searching import (
    binary_search,
    bmh_search,
    breadth_first_search,
    depth_first_search,
    kmp_search,
    rabinkarp_search,
    ternary_search
)


class TestBinarySearch(unittest.TestCase):
    """
    Tests Binary Search on a small range from 0-9
    """

    def test_binarysearch(self):
        self.seq = range(10)
        rv1 = binary_search.search(self.seq, 0)
        rv2 = binary_search.search(self.seq, 9)
        rv3 = binary_search.search(self.seq, -1)
        rv4 = binary_search.search(self.seq, 10)
        rv5 = binary_search.search(self.seq, 4)
        self.assertIs(rv1, 0)
        self.assertIs(rv2, 9)
        self.assertFalse(rv3)
        self.assertFalse(rv4)
        self.assertIs(rv5, 4)
        self.seq = range(9)
        rv1 = binary_search.search(self.seq, 0)
        rv2 = binary_search.search(self.seq, 8)
        rv3 = binary_search.search(self.seq, -1)
        rv4 = binary_search.search(self.seq, 10)
        rv5 = binary_search.search(self.seq, 4)
        self.assertIs(rv1, 0)
        self.assertIs(rv2, 8)
        self.assertFalse(rv3)
        self.assertFalse(rv4)
        self.assertIs(rv5, 4)


class TestBMHSearch(unittest.TestCase):
    """
    Tests BMH search on string "ABCDE FG ABCDEABCDEF"
    """

    def test_bmhsearch(self):
        self.string = "ABCDE FG ABCDEABCDEF"
        rv1 = bmh_search.search(self.string, "ABCDEA")
        rv2 = bmh_search.search(self.string, "ABCDER")
        self.assertIs(rv1[0], 9)
        self.assertFalse(rv2)


class TestBreadthFirstSearch(unittest.TestCase):
    """
    Tests DFS on a graph represented by a adjacency list
    """
    def test_bfs(self):
        self.graph = {
            'A': {'B', 'C'},
            'B': {'A', 'D', 'E'},
            'C': {'A', 'F'},
            'D': {'B'},
            'E': {'B', 'F'},
            'F': {'C', 'E'}
        }
        rv1 = breadth_first_search.bfs(self.graph, 'A')
        self.assertEqual(rv1, {'C', 'A', 'B', 'D', 'F', 'E'})
        self.graph = {
            'A': {'B', 'C', 'E'},
            'B': {'A', 'D', 'F'},
            'C': {'A', 'G'},
            'D': {'B'},
            'F': {'B'},
            'E': {'A'},
            'G': {'C'}
        }
        rv1 = breadth_first_search.bfs(self.graph, "A")
        rv2 = breadth_first_search.bfs(self.graph, "G")
        rv1e = breadth_first_search.bfs(self.graph, "Z")
        self.assertEqual(rv1, {'A', 'B', 'D', 'F', 'C', 'G', 'E'})
        self.assertEqual(rv2, {'G', 'C', 'A', 'B', 'D', 'F', 'E'})
        self.assertEqual(rv1e, None)


class TestDepthFirstSearch(unittest.TestCase):
    """
    Tests DFS on a graph represented by a adjacency list
    """

    def test_dfs(self):
        self.graph = {
            'A': ['B', 'C', 'E'],
            'B': ['A', 'D', 'F'],
            'C': ['A', 'G'],
            'D': ['B'],
            'F': ['B'],
            'E': ['A'],
            'G': ['C']
        }
        rv1 = depth_first_search.dfs(self.graph, "A")
        rv2 = depth_first_search.dfs(self.graph, "G")
        rv1e = depth_first_search.dfs(self.graph, "Z")
        self.assertEqual(rv1, ['A', 'B', 'D', 'F', 'C', 'G', 'E'])
        self.assertEqual(rv2, ['G', 'C', 'A', 'B', 'D', 'F', 'E'])
        self.assertEqual(rv1e, None)
        self.graph = {
            1: [2, 3, 4],
            2: [1, 6, 10],
            3: [1, 5, 10],
            4: [1, 10, 11],
            5: [3, 10],
            6: [2, 7, 8, 9],
            7: [6, 8],
            8: [6, 7],
            9: [6, 10],
            10: [3, 5, 9, 12],
            11: [4],
            12: [10]
        }
        rv3 = depth_first_search.dfs(self.graph, 1)
        rv4 = depth_first_search.dfs(self.graph, 5)
        rv5 = depth_first_search.dfs(self.graph, 6)
        rv2e = depth_first_search.dfs(self.graph, 99)
        self.assertEqual(rv3, [1, 2, 6, 7, 8, 9, 10, 3, 5, 12, 4, 11])
        self.assertEqual(rv4, [5, 3, 1, 2, 6, 7, 8, 9, 10, 12, 4, 11])
        self.assertEqual(rv5, [6, 2, 1, 3, 5, 10, 9, 12, 4, 11, 7, 8])
        self.assertEqual(rv2e, None)
        self.graph = {
            1: [2, 3, 4, 5, 6],
            2: [1, 4, 7, 8, 9],
            3: [1, 10],
            4: [1, 2, 11, 12],
            5: [1, 13, 14, 15],
            6: [1, 15],
            7: [2],
            8: [2],
            9: [2, 10],
            10: [3, 9],
            11: [4],
            12: [4],
            13: [5],
            14: [5],
            15: [5, 6]}
        rv6 = depth_first_search.dfs(self.graph, 1)
        rv7 = depth_first_search.dfs(self.graph, 10)
        rv8 = depth_first_search.dfs(self.graph, 5)
        rv3e = depth_first_search.dfs(self.graph, -1)
        self.assertEqual(
            rv6,
            [1, 2, 4, 11, 12, 7, 8, 9, 10, 3, 5, 13, 14, 15, 6]
        )
        self.assertEqual(
            rv7,
            [10, 3, 1, 2, 4, 11, 12, 7, 8, 9, 5, 13, 14, 15, 6]
        )
        self.assertEqual(
            rv8,
            [5, 1, 2, 4, 11, 12, 7, 8, 9, 10, 3, 6, 15, 13, 14]
        )
        self.assertEqual(rv3e, None)


class TestKMPSearch(unittest.TestCase):
    """
    Tests KMP search on string "ABCDE FG ABCDEABCDEF"
    """

    def test_kmpsearch(self):
        self.string = "ABCDE FG ABCDEABCDEF"
        rv1 = kmp_search.search(self.string, "ABCDEA")
        rv2 = kmp_search.search(self.string, "ABCDER")
        self.assertIs(rv1[0], 9)
        self.assertFalse(rv2)


class TestRabinKarpSearch(unittest.TestCase):
    """
    Tests Rabin-Karp search on string "ABCDEFGHIJKLMNOP"
    """

    def test_rabinkarpsearch(self):
        self.string = "ABCDEFGHIJKLMNOP"
        rv1 = rabinkarp_search.search(self.string, "MNOP")
        rv2 = rabinkarp_search.search(self.string, "BCA")
        self.assertIs(rv1[0], 12)
        self.assertFalse(rv2)


class TestTernarySearch(unittest.TestCase):
    """
    Tests teranry search algorithm on unimodal functions
    """

    def test_terarysearch(self):
        self.function1 = lambda x: -(x - 2) ** 2
        self.function2 = lambda x: math.cos(x)
        self.eps = 1e-6
        rv1 = ternary_search.search(self.function1, -2.0, 2.0, self.eps)
        rv2 = ternary_search.search(self.function2, -2.0, 2.0, self.eps)
        self.assertAlmostEqual(rv1, 2.0, 6)
        self.assertAlmostEqual(rv2, 0.0, 6)
