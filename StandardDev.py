import math
numElems=int(input())
elements=input().split()
elements = list(map(int, elements))
total=0
for i in range (len(elements)):
    total+=elements[i]
mean=total/numElems
summation = 0
for i in range (len(elements)):
    summation += pow(elements[i]-mean, 2)
print("%.1f" % (math.sqrt(summation/numElems)))
