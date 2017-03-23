def array_left_rotation(a, n, k):
    b = a[k:]+a[:k]
    return b


    return (a)
n, k = map(int, input().strip().split(' '))
a = list(map(int, input().strip().split(' ')))
answer = array_left_rotation(a, n, k);
print(*answer, sep=' ')
