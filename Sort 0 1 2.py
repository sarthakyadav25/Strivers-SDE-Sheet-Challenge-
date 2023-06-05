from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def Swap(arr,pos1,pos2):
    temp = arr[pos1]
    arr[pos1] = arr[pos2]
    arr[pos2] = temp

def sort012(arr, n) :
    low = 0
    high = n-1
    mid = 0
    while mid <= high:
        if arr[mid] == 0:
            Swap(arr,low,mid)
            low += 1
            mid += 1
        elif arr[mid] == 2:
            Swap(arr,high,mid)
            high -= 1
        else:
            mid += 1
    return arr


#taking inpit using fast I/O
def takeInput() :
	n = int(input().strip())

	if n == 0 :
		return list(), 0

	arr = list(map(int, stdin.readline().strip().split(" ")))

	return arr, n



def printAnswer(arr, n) :
    
    for i in range(n) :
        
        print(arr[i],end=" ")
        
    print()
    
#main

t = int(input().strip())
for i in range(t) :

    arr, n= takeInput()
    sort012(arr, n)
    printAnswer(arr, n)
