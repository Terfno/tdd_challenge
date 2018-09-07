import unittest
from add import ADD

class TestAdd(unittest.TestCase):
    def test_add(self):
        add = ADD()
        self.assertEqual(add.add(1,2), 3)
