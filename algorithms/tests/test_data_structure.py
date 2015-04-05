import unittest
from ..data_structure import stack,queue

class TestStack(unittest.TestCase):
    """
    Test Stack Implementation
    """
    def test_stack(self):
        self.sta = stack.stack()
        self.sta.add(5)
        self.sta.add(8)
        self.sta.add(10)
        self.sta.add(2)

        self.assertEqual(self.sta.remove(),2)
        self.assertEqual(self.sta.is_empty(),False)
        self.assertEqual(self.sta.size(),3)
        
class TestQueue(unittest.TestCase):
    """
    Test Queue Implementation
    """
    def test_queue(self):
        self.que = queue.queue()
        self.que.add(1)
        self.que.add(2)
        self.que.add(8)
        self.que.add(5)
        self.que.add(6)

        self.assertEqual(self.que.remove(),1)
        self.assertEqual(self.que.size(),4)
        self.assertEqual(self.que.remove(),2)
        self.assertEqual(self.que.remove(),8)
        self.assertEqual(self.que.remove(),5)
        self.assertEqual(self.que.remove(),6)
        self.assertEqual(self.que.is_empty(),True)
