from os import *
from sys import *
from collections import *
from math import *

def nextPermutation(nums,n):
    i = len(nums)-2
    while i >=0 and nums[i] >= nums[i+1]:
        i -= 1
    if i >= 0:
        j = len(nums)-1
        while nums[j] <= nums[i]:
            j -= 1
        temp = nums[j]
        nums[j] = nums[i]
        nums[i] = temp
    nums[i+1:len(nums)] = reversed(nums[i+1:len(nums)])
    return nums