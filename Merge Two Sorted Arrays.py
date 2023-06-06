from math import *
from collections import *
from sys import *
from os import *

def ninjaAndSortedArrays(arr1,arr2,m,n):
    cur = m+n-1
    p1 = m - 1
    p2 = n - 1
    while p1 >= 0 and p2 >= 0:
        if arr1[p1] > arr2[p2]:
            arr1[cur] = arr1[p1]
            p1 -= 1
        else:
            arr1[cur] = arr2[p2]
            p2 -= 1
        cur -= 1
    while p2 >= 0:
        arr1[cur] = arr2[p2]
        p2 -= 1
        cur -= 1
    return arr1
