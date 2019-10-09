__author__ = "Michael Falkenstein"

import unittest
from flatten import flatten


class TestFlatten(unittest.TestCase):
    '''
    This is a test class for flatten.py
    '''

    def test_empty_array(self):
        self.assertEqual(flatten([]), [])

    def test_flat_arrays(self):
    	self.assertEqual(flatten([1, 2, 5, 2, 2, 3, 4]), [1, 2, 5, 2, 2, 3, 4])
        self.assertEqual(flatten([1]), [1])

    def test_nested_arrays(self):
    	self.assertEqual(flatten([[1,2,[[5,[2,2],3]]],4]), [1, 2, 5, 2, 2, 3, 4])
        self.assertEqual(flatten([[1,2,[3]],4]), [1, 2, 3, 4])
        self.assertNotEqual(flatten([[]]), [[]])

if __name__ == '__main__':
    unittest.main()
