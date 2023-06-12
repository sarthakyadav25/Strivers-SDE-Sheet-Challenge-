from os import *
from sys import *
from collections import *
from math import *

def merge(arr, low1, high1, low2, high2):
    i1, j1 = low1, high1
    i2, j2 = low2, high2
    temp = []
    count = 0

    while i1 <= j1 and i2 <= j2:
        if arr[i1] <= arr[i2]:
            temp.append(arr[i1])
            i1 += 1
        else:
            temp.append(arr[i2])
            count += j1 - i1 + 1
            i2 += 1

    while i1 <= j1:
        temp.append(arr[i1])
        i1 += 1

    while i2 <= j2:
        temp.append(arr[i2])
        i2 += 1


    for i in range(low1, high2+1):
        arr[i] = temp[i - low1]

    return count


def merge_sort(arr, low, high):
    if low >= high:
        return 0

    mid = low + (high - low) // 2
    inv_count = 0

    inv_count += merge_sort(arr, low, mid)
    inv_count += merge_sort(arr, mid + 1, high)
    inv_count += merge(arr, low, mid, mid + 1, high)

    return inv_count


def getInversions(arr, n) :
    return merge_sort(arr,0,n-1)

# Taking inpit using fast I/O.
def takeInput() :
    n = int(input())
    arr = list(map(int, stdin.readline().strip().split(" ")))
    return arr, n

# Main.
arr, n = takeInput()
print(getInversions(arr, n))