import unittest


class FailingHookUpTest(unittest.TestCase):
    def test_two_plus_two(self):
        self.assertEqual(4, 2 + 2)
