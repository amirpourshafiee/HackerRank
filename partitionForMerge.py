def partition(ar):
    p=ar[0]
    eq,left,right=[],[],[]
    for i in ar:
        if i >= p:
            right.append(i)
        elif i <p:
            left.append(i)
    for t in left:
        print (t, end=" "),
    for k in right:
        print (k, end=" ")

m = input()
ar = [int(i) for i in input().strip().split()]
partition(ar)
