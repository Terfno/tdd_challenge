import unittest
from stack import STACK

class TestSTACK(unittest.TestCase):
    def test_isEmpty(self):
        stack=STACK()
        self.assertEqual(stack.isEmpty(), True)
    def test_push_top(self):
        stack=STACK()
        self.assertEqual(stack.top(),1)
