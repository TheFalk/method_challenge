__author__ = "Michael Falkenstein"

import unittest
from TempTracker import TempTracker


class TestTempTracker(unittest.TestCase):
    '''
    This is a test class for TempTracker.py
    '''

    def setUp(self):
    	self.tracker = TempTracker()

    def add_temp_values(self):
    	a = [1,2,3,4,1,3,9,99,1,0,5,109]
    	self.tracker.reset()
    	for x in a:
			self.tracker.insert(x)

    def test_mean(self):
    	self.tracker.reset()
        self.assertEqual(self.tracker.get_mean(), -1.0)
        self.add_temp_values()
        self.assertEqual(self.tracker.get_mean(), 19.75)

    def test_min(self):
    	self.tracker.reset()
        self.assertEqual(self.tracker.get_min(), -1)
        self.add_temp_values()
        self.assertEqual(self.tracker.get_min(), 0)

    def test_max(self):
    	self.tracker.reset()
        self.assertEqual(self.tracker.get_max(), -1)
        self.add_temp_values()
        self.assertEqual(self.tracker.get_max(), 109)

if __name__ == '__main__':
    unittest.main()
