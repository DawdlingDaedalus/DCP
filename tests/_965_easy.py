from problems._965_easy import isutf8
import numpy as np
import unittest


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
