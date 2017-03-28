# Complete the function below.


def  getMinimumUniqueSum(arr):
    l=[]
    for k in range(len(arr)):
        a=int(arr[k][0])
        b=int(arr[k][2])

        cnt = 0

        for i in range (a,b+1):
            j = 1;
            while j*j <= i:
                if j*j == i:
                    cnt = cnt+1


                j = j+1
            i = i+1
        l.append(cnt)


    l.append('\n')
    return l
