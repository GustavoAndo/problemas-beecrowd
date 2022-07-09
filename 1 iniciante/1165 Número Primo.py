n = int(input())
for i in range(n):
    p = int(input())
    c = 0
    for j in range(1, p+1):
        if p%j == 0: c += 1
    if c == 2: print(p, 'eh primo')
    else: print(p, 'nao eh primo')
