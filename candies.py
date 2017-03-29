
'''
Alice is a kindergarten teacher. She wants to give some candies to the children in her class.  All the children sit in a line ( their positions are fixed), and each  of them has a rating score according to his or her performance in the class.  Alice wants to give at least 1 candy to each child. If two children sit next to each other, then the one with the higher rating must get more candies. Alice wants to save money, so she needs to minimize the total number of candies given to the children.

Input Format

The first line of the input is an integer N, the number of children in Alice's class. Each of the following N lines contains an integer that indicates the rating of each child.

Constraints

Output Format

Output a single line containing the minimum number of candies Alice must buy.

Sample Input

3
1
2
2
Sample Output

4

'''
n = input()
a = [input() for _ in xrange(n)]
c, desc_buf = [1]*n, []

for i in xrange(1, n):
    if a[i] < a[i-1]:
        if not desc_buf:
            desc_buf = [i-1]
        desc_buf.append(i)
        if not i == n-1:
            continue
    if a[i] > a[i-1]:
        c[i] = c[i-1] + 1
    if desc_buf:
        for extra, idx in enumerate(desc_buf[::-1]):
            c[idx] = max(c[idx], extra + 1)
        del desc_buf[:]

print sum(c)
