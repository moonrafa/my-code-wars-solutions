""" Write a function that accepts an array of 10 integers (between 0 and 9),
that returns a string of those numbers in the form of a phone number
Example:
create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) => returns "(123) 456-7890"""
import unittest


def create_phone_number(n):
    ddd = str(n[0]) + str(n[1]) + str(n[2])
    p1 = str(n[3]) + str(n[4]) + str(n[5])
    p2 = str(n[6]) + str(n[7]) + str(n[8]) + str(n[9])
    return f'({ddd}) {p1}-{p2}'


class MyTestCase(unittest.TestCase):
    def test_create_phone_number(self):
        self.assertEqual(create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]), "(123) 456-7890")


if __name__ == '__main__':
    unittest.main()
