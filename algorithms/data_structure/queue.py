"""
   Queue data structure implemented:
   --------------------------------
   add : add element at last
   remove : remove element from front
            return value
   is_empty : 1 value returned on empty
              0 value returned on not empty
   size : return size of queue

   Time Complexity:  O(1)
"""
from collections import deque


class Queue:
    queue_list = deque([])

    def __init__(self):
        self.queue_list = deque([])

    def add(self, value):
        self.queue_list.append(value)

    def remove(self):
        return self.queue_list.popleft()

    def is_empty(self):
        return not len(self.queue_list)

    def size(self):
        return len(self.queue_list)
