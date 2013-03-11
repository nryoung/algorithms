Algorithms
==========

This is an attempt to build a cohesive module of algorithms in Python.

The purpose of this repo is to be a learning tool for myself and others.

I used psuedo code from various sources and I have listed them as references in the source code of each algorithm.

Algorithms implemented so far:
------------------------------

**Sorting:**

- Bogo Sort
- Bubble Sort
- Cocktail Sort
- Comb Sort
- Heap Sort
- Insertion Sort
- Merge Sort
- Quick Sort
- Selection Sort
- Shell Sort

**Searching:**

- Binary Search
- Boyer-Moore-Horspool
- Knuth-Morris-Pratt
- Rabin-Karp
- Depth First Search (Recursive)

**Shuffling:**

- Knuth/Fisher-Yates Shuffle

**Math:**

- Extended GCD

**Random:**

- Mersenne Twister


Installation:
-------------

To install, simply

::

    $ pip install algorithms


Usage:
------

Once installed you can simply do the following in your program:

::

    from algorithms.sorting import bubble_sort

    my_list = bubble_sort.sort(my_list)


All prequisites for the algorithms are listed in the source code for each algorithm.


Tests:
------

Nose is used as the main test runner and all Unit Tests can be run by: 

::

    $ python algorithms/run_tests.py


Contributing:
-------------

If there is an algorithm or data structure that you do not see, but would like to add please feel free to do a pull request. I only ask two things:

1. For each algorithm and data structure you implement please have corresponding unit tests to prove correctness.
2. Please make sure that your module follows similar style guidelines that are laid out in the other modules.

I want to personally thank everybody that has contributed so far and your names will be added to `AUTHORS.rst`.


TODO:
-----

See `TODO.rst`.


License:
--------

Copyright (c) 2012 by Nic Young and contributors. See AUTHORS.rst for more details

Some rights reserved.

Redistribution and use in source and binary forms of the software as well as documentation, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

* The names of the contributors may not be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE AND DOCUMENTATION IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE AND DOCUMENTATION, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
