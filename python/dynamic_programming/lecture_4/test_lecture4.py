from unittest import TestCase

from lecture_4.lecture4 import climbing_stairs


class Test(TestCase):
    def test_climbing_stairs(self):
        self.assertEqual(climbing_stairs(100), 573147844013817084101)
        self.assertEqual(climbing_stairs(5), 8)
        self.assertEqual(climbing_stairs(2), 2)
        self.assertEqual(climbing_stairs(1), 1)
        self.assertEqual(climbing_stairs(0), 1)
