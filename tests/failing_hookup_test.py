import unittest


class FailingHookUpTest(unittest.TestCase):
    def test_two_plus_two(self):
        self.assertEqual(5, 2 + 2)
