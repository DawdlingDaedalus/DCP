"""
UTF-8 is a character encoding that maps each symbol to one, two, three, or four bytes.

For example, the Euro sign, €, 
corresponds to the three bytes 11100010 10000010 10101100. 
The rules for mapping characters are as follows:

For a single-byte character, the first bit must be zero.
For an n-byte character, the first byte starts with n ones and a zero. 
The other n - 1 bytes all start with 10.
Visually, this can be represented as follows.

 Bytes   |           Byte format
-----------------------------------------------
   1     | 0xxxxxxx
   2     | 110xxxxx 10xxxxxx
   3     | 1110xxxx 10xxxxxx 10xxxxxx
   4     | 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

Write a program that takes in an array of integers representing byte values, 
and returns whether it is a valid UTF-8 encoding.
"""

import numpy as np
import unittest


def isbinrep(arr: np.array):
    """ determines if array is binary representative (1s and 0s only)"""
    bad_list = []
    for i in range(len(arr)):
        if (arr[i] != 0) and (arr[i] != 1):
            bad_list.append(arr[i])
    if bad_list:
        print("Some numbers do not represent binary")
        return False
    else:
        return True


def isutf8(arr: np.array):
    """ takes array of integers representing bit values,
        returns True if valid UTF-8 encoding.
    """
    if type(arr) != np.ndarray:  # sanitize for input
        print("input was not a numpy.ndarray")
        return False

    if arr[0] == 0:  # code for 1 byte format check
        if len(arr) == 8 and isbinrep(arr):
            print("True")
            return True
        else:
            print("False")
            return False

    # code for 2 byte format check
    elif (np.array_equal(arr[:3], np.array([1, 1, 0]))) and isbinrep(arr):
        if len(arr) == 16:
            print("True")
            return True
        else:
            print("False")
            return False

    # code for 3 byte format check
    elif (np.array_equal(arr[:4], np.array([1, 1, 1, 0]))) and isbinrep(arr):
        if len(arr) == 24:
            print("True")
            return True
        else:
            print("False")
            return False

    # code for 4 byte format check
    elif (np.array_equal(arr[:5], np.array([1, 1, 1, 1, 0]))) and isbinrep(arr):
        if len(arr) == 32:
            print("True")
            return True
        else:
            print("False")
            return False
    else:
        print("array was not of correct length to be UTF-8")


# tests
class Test_isutf8(unittest.TestCase):
    def test_1_byte_format(self):
        self.assertEqual(isutf8(np.array([0, 1, 0, 1, 0, 1, 0, 1])), True)

    def test_2_byte_format(self):
        self.assertEqual(
            isutf8(np.array([1, 1, 0, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1])), True)

    def test_3_byte_format(self):
        self.assertEqual(isutf8(np.array(
            [1, 1, 1, 0, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), True)

    def test_4_byte_format(self):
        self.assertEqual(isutf8(np.array(
            [1, 1, 1, 1, 0, 1, 0, 1, 1, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1])), True)

    def test_not_binary(self):
        self.assertEqual(isutf8(np.array([0, 1, 0, 1, 9, 0, 0, 0])), False)

    def test_string_input(self):
        self.assertEqual(isutf8("string input"), False)

    def test_float_input(self):
        self.assertEqual(isutf8(90.4462), False)

    def test_extra_argument(self):
        with self.assertRaises(TypeError):
            isutf8(648, "string")


if __name__ == '__main__':
    unittest.main()
