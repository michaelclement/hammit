import unittest
from src.hammit.distance import distance

class TestDistance(unittest.TestCase):
    def test_distance(self):
        self.assertEqual(distance('123','122'), 1)
    def test_distance_bad_input(self):
        self.assertEqual(distance('1234', '123'), -1)

unittest.main()
