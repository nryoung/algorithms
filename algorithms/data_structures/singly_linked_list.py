"""
    Singly Linked List
    ------------------
    A linked list is a data structure consisting of a group of nodes which
    together represent a sequence. Under the simplest form, each node is
    composed of data and a reference (in other words, a link) to the next
    node in the sequence; more complex variants add additional links. This
    structure allows for efficient insertion or removal of elements from any
    position in the sequence.

    Pseudo Code: https://en.wikipedia.org/wiki/Linked_list
"""


class Node:

    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

    def set_data(self, data):
        self.data = data

    def get_data(self):
        return self.data

    def set_next(self, next):
        self.next = next

    def get_next(self):
        return self.next


class SinglyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0

    def add(self, value):
        """
        Add element to list

        Time Complexity:  O(N)
        """
        node = Node(value)
        node.set_next(self.head)
        self.head = node
        self.size += 1

    def _search_node(self, value, remove=False):
        current = self.head
        previous = None

        while current:
            if current.data == value:
                break
            else:
                previous = current
                current = current.next

        if remove and current:
            if previous is None:  # Head node
                self.head = current.next
            else:  # None head node
                previous.set_next(current.next)
            self.size -= 1

        return current is not None

    def remove(self, value):
        """
        Remove element from list

        Time Complexity:  O(N)
        """

        return self._search_node(value, True)

    def search(self, value):
        """
        Search for value in list

        Time Complexity:  O(N)
        """
        return self._search_node(value)

    def size(self):
        """
        Return size of list
        """
        return self.size
