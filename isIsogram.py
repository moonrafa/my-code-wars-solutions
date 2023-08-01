"""An isogram is a word that has no repeating letters, consecutive or non-consecutive.
Implement a function that determines whether a string that contains only letters is an isogram.
Assume the empty string is an isogram. Ignore letter case.

Example:

isIsogram "Dermatoglyphics" = true
isIsogram "moose" = false
isIsogram "aba" = false"""
import unittest


def is_isogram(string):
    set_transform = set(string.lower())
    if len(string) > len(set_transform):
        return False
    else:
        return True


class TestCases(unittest.TestCase):
    def test_is_isogram(self):
        self.assertEqual(is_isogram("Dermatoglyphics"), True)
        self.assertEqual(is_isogram("isogram"), True)
        self.assertEqual(is_isogram("aba"), False)
        self.assertEqual(is_isogram("moOse"), False)
        self.assertEqual(is_isogram("isIsogram"), False)
        self.assertEqual(is_isogram(""), True)


if __name__ == '__main__':
    unittest.main()
