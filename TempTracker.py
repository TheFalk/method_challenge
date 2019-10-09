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

	'''

	def __init__(self):
		self.data = []
		self.total = 0.0 # Saves on computation time

	def insert(self, temp):
		'''records a new temperature.

		Arg:
			temp (int): temperature to be recorded

		'''
		if self.get_mean() == -1.0:
			self.data.append(temp)
		else:
			if temp >= self.data[-1]:
				self.data.append(temp)
			elif temp < self.data[0]:
				self.data.insert(0,temp)
			else:
				self.data.insert(-1,temp)
		self.total += temp
		return

	def get_mean(self):
		'''returns the mean of all temps we've seen so far.

		Note:
			If no temperatures have been recorded, -1.0 is returned

		Returns:
			float: Average of all temperatures recorded

		'''
		sz = len(self.data)
		if sz is 0:
			return -1.0
		else:
			return self.total/sz

	def get_max(self):
		'''returns the highest temp we've seen so far.
		
		Note:
			If no temperatures have been recorded, -1 is returned

		Returns:
			int: The last value of the data array.

		'''
		if len(self.data) is 0:
			return -1
		else:
			return self.data[-1]

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
			return self.data[0]

	def reset(self):
		'''
		clears data for testing
		'''
		self.data = []
		self.total = 0.0
		return
