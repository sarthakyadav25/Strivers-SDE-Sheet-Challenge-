from os import *
from sys import *
from collections import *
from math import *

def maximumProfit(prices):
    n = len(prices)
    prevmin = prices[0]
    ans = 0
    for i in range(1,n):
        profit = prices[i] - prevmin
        ans = max(ans,profit)
        prevmin = min(prevmin,prices[i])
    return ans