#!/bin/python3

import sys


n = int(input().strip())
arr = [int(arr_temp) for arr_temp in input().strip().split(' ')]
total = 0
for i in range(n):
    total+=arr[i]
print (total)
