Algorithms: a module of useful algorithms for Python
====================================================

This is an attempt to build a cohesive module of algorithms for Python. 

The purpose of this repo is to be a learning tool for myself and others.

I used psuedo code from various sources and I have listed them as references in the source code of each algorithm.

Algorithms implemented so far:
------------------------------

**Sorting:**
    - Bubble Sort
    - Comb Sort
    - Heap Sort
    - Insertion Sort
    - Quick Sort
    - Selection Sort
    - Shell Sort

**Searching:**
    - Binary Search
    - Knuth-Morris-Pratt

Installation:
-------------

Requirements are listed in :code:`requirements.txt`.

If you are using pip and virtualenv you can simply do: 

::
    $ pip install -r requirements.txt

To clone the repository simply: 

::
    $ git clone https://github.com/nryoung/algorithms.git

in to your working directory.

Usage:
------

Once cloned you can simply do the following in your program:

.. code:: python

    from algorithms.sorting import bubble_sort

    my_list = bubble_sort.sort(my_list)

All prequisites for the algorithms are listed in the source code for each algorithm.

Tests:
------------------------

Nose is used as the main test runner and all Unit Tests can be run by: 

::
    $ python algorithms/run_tests.py

TODO:
-----

Below is an ever changing list of things that I would like to accomplish or implement. If you feel something needs to be added simply do a pull request.

**Algorithms to implement:**
    - Rabin-Karp
    - Mersenne Twister
    - UUID Generator
    - Bloom Filters

**Misc.:**
    - Performance Tests

License:
--------

Copyright (c) 2012 by Nic Young and contributors. 

Some rights reserved.

Redistribution and use in source and binary forms of the software as well as documentation, with or without modification, are permitted provided that the following conditions are met:

* Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

* Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

* The names of the contributors may not be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE AND DOCUMENTATION IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE AND DOCUMENTATION, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
