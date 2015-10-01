"""
   Stack data structure implemented:
   --------------------------------
   add : add element at last
   remove : remove element from last
            return value
   is_empty : 1 value returned on empty
              0 value returned on not empty
   size : return size of stack

   Time Complexity:  O(1)
"""


class Stack:
    stack_list = []

    def __init__(self):
        self.stack_list = []

    def add(self, value):
        self.stack_list.append(value)

    def remove(self):
        return self.stack_list.pop()

    def is_empty(self):
        return not len(self.stack_list)

    def size(self):
        return len(self.stack_list)
