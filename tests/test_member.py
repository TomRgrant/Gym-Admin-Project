import unittest
from models.member import Member

class TestMember(unittest.TestCase):
    def setUp(self):
        self.member = Member("Tom", "Grant", True)

    def test_member_has_first_name(self):
        expected = "Tom"
        actual = self.member.first_name
        self.assertEqual(expected, actual)

    def test_member_has_last_name(self):
        expected = "Grant"
        actual = self.member.last_name
        self.assertEqual(expected, actual)

    def test_has_membership__True(self):
        expected = True
        actual = self.member.membership
        self.assertEqual(expected, actual)

    def test_has_membership__False(self):
        member_1 = Member("Jeff", "Newits", False)
        expected = False
        actual = member_1.membership
        self.assertEqual(expected, actual)
