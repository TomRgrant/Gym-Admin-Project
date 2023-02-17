import unittest
from models.gym_class import Gym_class
import datetime

class TestGymClass(unittest.TestCase):
    def setUp(self):
        self.gym_class = Gym_class("Spin Class", "Learn how to spin", "Alex Jonna", datetime.date(2023, 4, 14))

    def test_gym_class_has_title(self):
        expected = "Spin Class"
        actual = self.gym_class.title
        self.assertEqual(expected, actual)

    def test_gym_class_has_description(self):
        expected = "Learn how to spin"
        actual = self.gym_class.description
        self.assertEqual(expected, actual)

    def test_gym_class_has_instructor(self):
        expected = "Alex Jonna"
        actual = self.gym_class.instructor
        self.assertEqual(expected, actual)

    def test_gym_class_has_date(self):
        expected = datetime.date(2023, 4, 14)
        actual = self.gym_class.class_date
        self.assertEqual(expected, actual)