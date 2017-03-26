#!/bin/python3

import sys

grade=[]
n = int(input().strip())
for a0 in range(n):
    grade.append(int(input().strip()))
    # your code goes here

for i in range (n):
    if grade[i] >=38:
        if grade[i]%5 >=3:
            grade[i]= grade[i] +(5- grade[i]%5)
    print(grade[i])
  
