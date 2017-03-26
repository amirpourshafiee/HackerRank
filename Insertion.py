size=int(input())
ar= [int(i) for i in input().strip(' ').split()]
target=ar[size-1]
i=1
while(ar[size-i-1])>=target and i<= size-1:
    ar[size-i] = ar[size-i-1]
    i+=1
    print(' '.join(map(str, ar)))
else:
    ar[size-i] = target
    print(' '.join(map(str, ar)))
