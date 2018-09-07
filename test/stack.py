import unittest
from stack import STACK

class TestSTACK(unittest.TestCase):
    def test_push(self):
        stack=STACK()
        self.assertEqual(stack.isEmpty(), True)