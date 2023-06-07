from math import *
from collections import *
from sys import *
from os import *

def findMajorityElement(nums, length):
	counter  = 1
	majority = nums[0]
	for i in range(1,length):
		if nums[i] == majority:
			counter += 1
		else:
			counter -= 1
			if counter == 0:
				counter = 1
				majority = nums[i]
	counter = 0
	for i in nums:
		if i == majority:
			counter += 1
	if counter > length//2:
		return majority
	return -1