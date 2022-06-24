q = int(input())
dic = {}
contdic = {}

def fib(n):
    if n == 0: return 0     
    if n == 1: return 1
    if n not in dic:
        dic[n] = fib(n-1) + fib(n-2)
    return dic[n]

def cont(n):
    if n == 0 or  n == 1: return 0     
    if n not in contdic:
        contdic[n] = cont(n-1) + cont(n-2) + 2
    return contdic[n]

for i in range(q):
    n = int(input())
    fib = fib(n)
    cont = cont(n)
    print('fib({0}) = {1} calls = {2}'.format(n, cont, fib))
