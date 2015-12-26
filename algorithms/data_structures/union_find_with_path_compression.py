"""
    Union Find with path compression
    --------------------------------
    A disjoint-set data structure, also called union-find data structure
    implements two functions:

    union(A, B) - merge A's set with B's set

    find(A) - finds what set A belongs to

    Union with path compression approach:

    Each node visited on the way to a root node may as well be attached
    directly to the root node.
    attach the smaller tree to the root of the larger tree

    Time Complexity  :  O(a(n)), where a(n) is the inverse of the function
    n=f(x)=A(x,x) and A is the extremely fast-growing Ackermann function.

    Psuedo Code: http://en.wikipedia.org/wiki/Disjoint-set_data_structure
"""


class UnionFindWithPathCompression:
    def __init__(self, N):
        if type(N) != int:
            raise TypeError("size must be integer")
        if N < 0:
            raise ValueError("N cannot be a negative integer")
        self.__parent = []
        self.__rank = []
        self.__N = N
        for i in range(0, N):
            self.__parent.append(i)
            self.__rank.append(0)

    def make_set(self, x):
        if type(x) != int:
            raise TypeError("x must be integer")
        if x != self.__N:
            raise ValueError(
                "a new element must have index {0}".format(self.__N))
        self.__parent.append(x)
        self.__rank.append(0)
        self.__N = self.__N + 1

    def union(self, x, y):
        self.__validate_ele(x)
        self.__validate_ele(y)
        x_root = self.__find(x)
        y_root = self.__find(y)
        if x_root == y_root:
            return
        # x and y are not already in same set. Merge them
        if self.__rank[x_root] < self.__rank[y_root]:
            self.__parent[x_root] = y_root
        elif self.__rank[x_root] > self.__rank[y_root]:
            self.__parent[y_root] = x_root
        else:
            self.__parent[y_root] = x_root
            self.__rank[x_root] = self.__rank[x_root] + 1

    def __find(self, x):
        if self.__parent[x] != x:
            self.__parent[x] = self.__find(self.__parent[x])
        return self.__parent[x]

    def find(self, x):
        self.__validate_ele(x)
        if self.__parent[x] == x:
            return x
        else:
            return self.find(self.__parent[x])

    def is_connected(self, x, y):
        self.__validate_ele(x)
        self.__validate_ele(y)
        return self.find(x) == self.find(y)

    # use for unit testing check if the path is compressed
    def parent(self, x):
        return self.__parent[x]

    def __validate_ele(self, x):
        if type(x) != int:
            raise TypeError("{0} is not an integer".format(x))
        if x < 0 or x >= self.__N:
            raise ValueError("{0} is not in [0,{1})".format(x, self.__N))
