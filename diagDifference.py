#!/bin/python3


import sys

n = int(input().strip())
dSumLeft  = 0
dSumRight  = 0
for i in range(n):
    matrixRow = list(map(int,input().strip().split(' ')))
    dSumLeft += int(matrixRow[i])
    dSumRight += int(matrixRow[n-i-1])
print (abs(dSumLeft - dSumRight))
