def fibonacci2(n):
    # Write your code here.
    if n==0:
        result = 0
    elif n==1:
        result = 1
    else:
        result = (fibonacci(n-1)+fibonacci(n-2))
    return result

memory = {}
def fibonacci(n):
    if n < 2:
        return n
    if not n in memory.keys():
        memory[n] = fibonacci(n-1) + fibonacci(n-2)
    return memory[n]


n = int(input())
print(fibonacci(n))
