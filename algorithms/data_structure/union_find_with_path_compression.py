"""
    union_find_with_path_compression.py
    An implementation of union find with path compression data structure.
    Union Find Overview:
    ------------------------
    A disjoint-set data structure, also called union-find data structure implements two functions:
        union(A, B) - merge A's set with B's set
        find(A) - finds what set A belongs to
    Union with path compression approach:
        Each node visited on the way to a root node may as well be attached directly to the root node.
        attach the smaller tree to the root of the larger tree
    Time Complexity  :  O(a(n)), where a(n) is the inverse of the function n=f(x)=A(x,x) and A is the extremely fast-growing Ackermann function.
    Psuedo Code: http://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""
class UnionFindWithPathCompression:
    def __init__(self, N):
        if type(N) != int:
            raise TypeError, "size must be integer"
        if N < 0:
            raise ValueError, "N cannot be a negative integer"
        self.parent = []
        self.rank = []
        self.N  = N
        for i in range(0, N):
            self.parent.append(i)
            self.rank.append(0)

    def make_set(self, x):
        if type(x) != int:
            raise TypeError, "x must be integer"
        if x != self.N:
            raise ValueError, "a new element must have index {0} since the total num of elements is {0}".format(self.N)
        self.parent.append(x)
        self.rank.append(0)
        self.N = self.N + 1

    def union(self, x, y):
        self.__validate_ele(x)
        self.__validate_ele(y)
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        # x and y are not already in same set. Merge them
        if self.rank[x_root] < self.rank[y_root]:
            self.parent[x_root] = y_root
        elif self.rank[x_root] > self.rank[y_root]:
            self.parent[y_root] = x_root
        else:
            self.parent[y_root] = x_root
            self.rank[x_root] = self.rank[x_root] + 1

    def __find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.__find(self.parent[x])
        return self.parent[x]

    def find(self, x):
        self.__validate_ele(x)
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])

    def is_connected(self, x, y):
        self.__validate_ele(x)
        self.__validate_ele(y)
        return self.find(x) == self.find(y)

    def __validate_ele(self, x):
        if type(x) != int:
            raise TypeError, "{0} is not an integer".format(x)
        if x < 0 or x >= self.N:
            raise ValueError, "{0} is not in [0,{1})".format(x, self.N)

