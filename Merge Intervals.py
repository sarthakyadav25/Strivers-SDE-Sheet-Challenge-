from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit

class Solution:
    def __init__ (self, start, end):
        self.start = start
        self.end = end

def mergeIntervals(intervals):
    intervals.sort(key = lambda x : x.start)
    start = intervals[0].start
    end = intervals[0].end
    ans = []
    for i in range(1,len(intervals)):
        newstart = intervals[i].start
        newend = intervals[i].end
        if newstart <= end and newend > end:
            end = newend
        elif newstart <= end and newend <= end:
            continue
        else:
            ans.append(Solution(start,end))
            start = newstart
            end = newend
    ans.append(Solution(start,end))
    return ans


n = int(input())
arr1 = list(map(int, stdin.readline().strip().split(" ")))
arr2 = list(map(int, stdin.readline().strip().split(" ")))
arr1.sort()
arr2.sort()
intervals = []
for i in range(n):
    a = Solution(arr1[i], arr2[i])
    intervals.append(a)

res = mergeIntervals(intervals)

for i in range(len(res)):
    print(res[i].start, res[i].end)
