numElems=int(input())
vals=input().split()
vals = list(map(int, vals))
total= 0
for i in range (0, len(vals)):
    total += vals[i]
print("%.1f" % (total/numElems))
vals=sorted(vals)

if numElems%2 == 0:
    median=(vals[numElems//2]+vals[numElems//2-1])/2
else:
    median=vals[numElems//s]
print("%.1f" % (median))
counter = 0
L=[]
mode=0
high=0
for i in range (0, len(vals)):

    L.append(vals.count(vals[i]))
    if high<max(L):

        high=max(L)

        mode=vals[i]

print(mode)
