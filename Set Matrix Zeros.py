from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(matrix: List[List[int]]) -> None:
        n = len(matrix)
        m = len(matrix[0])
        rowarr = [0]*n
        colarr = [0]*m
        flag = False
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    if i == 0:
                        flag = True
                        matrix[0][j] = -float("inf")
                    else:
                        matrix[i][0] = -float("inf")
                        matrix[0][j] = -float("inf")
        for i in range(1,n):
            if matrix[i][0] == -float("inf"):
                for j in range(m):
                    matrix[i][j] = 0
        for i in range(m):
            if matrix[0][i] == -float("inf"):
                for j in range(n):
                    matrix[j][i] = 0
        if flag == True:
            for i in range(m):
                matrix[0][i] = 0
        return matrix