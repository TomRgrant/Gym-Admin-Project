import unittest
from models.visit import Visit

class TestVisit(unittest.TestCase):
    def setUp(self):
        self.visit = Visit(1, 5)

    def test_has_member(self):
        expected = 1
        actual = self.visit.member
        self.assertEqual(expected, actual)

    def test_has_gym_class(self):
        expected = 5
        actual = self.visit.gym_class
        self.assertEqual(expected, actual)