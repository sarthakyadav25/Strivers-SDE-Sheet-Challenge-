from os import *
from sys import *
from collections import *
from math import *

def printPascal(n:int):
    ansarr = [[] for i in range(n)]
    ansarr[0].append(1)
    prev = ansarr[0]
    for i in range(1,n):
        ansarr[i].append(1)
        for j in range(len(prev)-1):
            ansarr[i].append(prev[j]+prev[j+1])
        ansarr[i].append(1)
        prev = ansarr[i]
    return ansarr