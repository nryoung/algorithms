"""
    union_find.py
    A Naive Implementation of union find data structure.
    Union Find Overview:
    ------------------------
    A disjoint-set data structure, also called union-find data structure implements two functions:
        union(A, B) - merge A's set with B's set
        find(A) - finds what set A belongs to
    Navie approach:
        Find follows parent nodes until it reaches the root.
        Union combines two trees into one by attaching the root of one to the root of the other
    Time Complexity  :  O(N) (a highly unbalanced tree might be created, nothing better a linked-list)
    Psuedo Code: http://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""
class UnionFind:
    def __init__(self, N):
        if type(N) != int:
            raise TypeError, "size must be integer"
        if N < 0:
            raise ValueError, "N cannot be a negative integer"
        self.forests = []
        self.N  = N
        for i in range(0, N):
            self.forests.append(i)

    def make_set(self, x):
        if type(x) != int:
            raise TypeError, "x must be integer"
        if x != self.N:
            raise ValueError, "a new element must have index {0} since the total num of elements is {0}".format(self.N)
        self.forests.append(x)
        self.N = self.N + 1

    def union(self, x, y):
        self.__validate_ele(x)
        self.__validate_ele(y)
        x_root = self.find(x)
        y_root = self.find(y)
        self.forests[x_root] = y_root

    def find(self, x):
        self.__validate_ele(x)
        if self.forests[x] == x:
            return x
        else:
            return self.find(self.forests[x])

    def is_connected(self, x, y):
        self.__validate_ele(x)
        self.__validate_ele(y)
        return self.find(x) == self.find(y)

    def __validate_ele(self, x):
        if type(x) != int:
            raise TypeError, "{0} is not an integer".format(x)
        if x < 0 or x >= self.N:
            raise ValueError, "{0} is not in [0,{1})".format(x, self.N)
