V=int(input())
size=int(input())
ar= [int(i) for i in input().strip().split()]
for i in range (size):
    if V==ar[i]:
        print (i)
  
