#!/bin/python3

import sys

positive=negative=zeroes = 0
n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
for i in range (n):
    if arr[i]>0:
        positive+=1
    elif arr[i]<0:
        negative+=1
    else:
        zeroes+=1
print (str(positive/n) + "\n"+ str(negative/n) + "\n" + str(zeroes/n))
