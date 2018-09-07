import unittest
from stack import STACK

class TestSTACK(unittest.TestCase):
    def setUp(self):
        stack=STACK()
    def test_isEmpty(self):
        self.assertEqual(stack.isEmpty(), True)
    def test_push_top(self):
        self.assertEqual(stack.top(),1)
