'''

This module contains the function flatten.
Flatten will take an array of arbitrarily nested arrays of integers into a
flat array of integers. e.g. [[1,2,[3]],4] -> [1,2,3,4].

Example:
	ar =  [[1,2,[[5,[2,2],3]]],4]
	print flatten(ar)
	[1, 2, 5, 2, 2, 3, 4]

Todo:
	Add error-checking for inputs

'''

__author__ = "Michael Falkenstein"


def flatten(arr):
	'''flatten function.

	Args:
		arr (array or int): Takes either an array to flatten or an int

	Returns:
		array: Returns either a flattened array or an int to return as an array

	'''
	if type([]) is type(arr):
		nArr = []
		for x in arr:
			nArr.extend(flatten(x))
		return nArr
	return [arr]
