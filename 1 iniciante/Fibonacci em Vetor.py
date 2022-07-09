dic = {}

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    if n not in dic: dic[n] = fib(n-1) + fib(n-2)
    return dic[n]

q = int(input())
for i in range(q):
    n = int(input())
    print('Fib(' + str(n) + ') = ' + str(fib(n)))
    
