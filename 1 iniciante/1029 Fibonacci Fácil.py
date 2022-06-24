dic = {}
def fib(n):
    if n == 1: return 0
    elif n == 2: return 1
    if n not in dic:
        dic[n] = fib(n-1) + fib(n-2)
    return dic[n]

n = int(input())
fib(n)
if n >= 1: print('0', end=' ')
if n >= 2: print('1', end=' ') 
for i in dic:
    if i == len(dic)+2: print(dic[i])
    else: print(dic[i], end=' ')
    
