q = int(input())
for i in range(q):
    l = [int(n) for n in input().split()]
    x = min(l)
    y = max(l)
    s = 0
    for j in range(x+1, y):
        if j % 2 == 1: s += j
    print(s)
