from math import *
from collections import *
from sys import *
from os import *

def missingAndRepeating(arr, n):
    hashmap = {}
    for i in range(n):
        if arr[i] not in hashmap:
            hashmap[arr[i]] = i
        else:
            repeat = arr[i]
    for i in range(1,n+1):
        if i not in hashmap:
            return [i,repeat]