Algorithms
==========

.. image:: https://travis-ci.org/nryoung/algorithms.svg?branch=master
    :target: https://travis-ci.org/nryoung/algorithms

.. image:: http://codecov.io/github/nryoung/algorithms/coverage.svg?branch=master
    :target: http://codecov.io/github/nryoung/algorithms?branch=master

This is an attempt to build a cohesive module of algorithms in Python.

The purpose of this repo is to be a learning tool for myself and others.

I used psuedo code from various sources and I have listed them as references in the source code of each algorithm.

Algorithms implemented so far:
------------------------------

**Data Structures:**

- Queue
- Stack
- Disjoint Set
- Single Linked List
- Undirected Graph
- Digraph

**Sorting:**

- Bogo Sort
- Bubble Sort
- Cocktail Sort
- Comb Sort
- Heap Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- In Place Quick Sort
- Selection Sort
- Shell Sort
- Gnome Sort
- Strand Sort

**Searching:**

- Binary Search
- Boyer-Moore-Horspool
- Knuth-Morris-Pratt
- Rabin-Karp
- Depth First Search (Recursive)
- Breadth First Search (Iterative)

**Shuffling:**

- Knuth/Fisher-Yates Shuffle

**Math:**

- Extended GCD
- Standard Normal Probability Density Function
- Cumulative Density Function (Approximation; 16 digit precision for 300 iter.)
- Sieve of Eratosthenes

**Dynamic Programming:**

- Longest Common Subsequence

**Random:**

- Mersenne Twister


Installation:
-------------

If you want to use the algorithms directly, simply

::

    $ pip install algorithms

If you want to examine the algorithms source, then you should clone this repo.

Usage:
------

Once installed you can simply do the following in your program:

::

    from algorithms.sorting import bubble_sort

    my_list = bubble_sort.sort(my_list)


All prequisites for the algorithms are listed in the source code for each algorithm.


Tests:
------

Pytest is used as the main test runner and all Unit Tests can be run with:

::

    $ ./run_tests.py


Contributing:
-------------

If there is an algorithm or data structure that you do not see, but would like to add please feel free to do a pull request. I only ask two things:

1. For each algorithm and data structure you implement please have corresponding unit tests to prove correctness.
2. Please make sure that your module follows similar style guidelines that are laid out in the other modules.

I want to personally thank everybody that has contributed so far and your names will be added to `AUTHORS.rst`.


TODO:
-----
See `TODO.rst`_.

.. _`TODO.rst`: TODO.rst
