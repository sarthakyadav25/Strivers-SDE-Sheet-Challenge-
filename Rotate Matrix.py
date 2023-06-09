from math import *
from collections import *
from sys import *
from os import *

def rotateMatrix(mat, n, m):
    sr = 0
    sc = 0
    er = n
    ec = m
    while sr < er-1 and sc < ec-1:
        val = mat[sr][sc]
        for col in range(sc+1,ec):
            temp = mat[sr][col]
            mat[sr][col] = val
            val = temp

        for row in range(sr+1,er):
            temp = mat[row][ec-1]
            mat[row][ec-1] = val
            val = temp

        for col in range(ec-2,sc-1,-1):
            temp = mat[er-1][col]
            mat[er-1][col] = val
            val = temp
        
        for row in range(er-2,sr-1,-1):
            temp = mat[row][sc]
            mat[row][sc] = val
            val = temp

        sr += 1
        sc += 1
        er -= 1
        ec -= 1

    
    
