'''

This module contains the class TempTracker.
TempTracker records a number of temperatures, and at any point could
return the minimum, maximum, or mean of the given temperatures.

Todo:
	Add error-checking for function inputs

'''

__author__ = "Michael Falkenstein"


class TempTracker(object):
	'''Exceptions are documented in the same way as classes.

	Attributes:
		data (array): Array containing the list of recorded temperatures
		total (float): Combined value for all recorded temperatures.
		not_empty (bool): Describing whether temperatures have been recorded

	'''

	def __init__(self):
		self.data = []
		self.total = 0.0 # Saves on computation time
		self.not_empty = False

	def insert(self, temp):
		'''records a new temperature.

		Arg:
			temp (int): temperature to be recorded

		'''
		if self.not_empty:
			if temp >= self.data[-1]: # Checking end of array for highest temp
				self.data.append(temp)
			elif temp < self.data[0]: # Checking beginning of array for lowest temp
				self.data.insert(0,temp)
			else:
				self.data.insert(-1,temp) # Neither high or low, gets inserted in the middle
		else:
			self.data.append(temp)
			self.not_empty = True
		self.total += temp
		return

	def get_mean(self):
		'''returns the mean of all temps we've seen so far.

		Note:
			If no temperatures have been recorded, -1.0 is returned

		Returns:
			float: Average of all temperatures recorded

		'''
		size = len(self.data)
		if size is 0:
			return -1.0
		else:
			return self.total/size

	def get_max(self):
		'''returns the highest temp we've seen so far.
		
		Note:
			If no temperatures have been recorded, -1 is returned

		Returns:
			int: The last value of the data array.

		'''
		return self.data[-1] if self.not_empty else -1

	def get_min(self):
		'''returns the lowest temp we've seen so far.

		Note:
			If no temperatures have been recorded, -1 is returned

		Returns:
			int: The first value of the data array.

		'''
		if len(self.data) is 0:
			return -1
		else:
		return self.data[] if self.not_empty else -1

	def reset(self):
		'''
		clears data for testing
		'''
		self.data = []
		self.total = 0.0
		self.not_empty = False
		return
