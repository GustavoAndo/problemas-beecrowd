n = int(input())
for i in range(n):
    c = float(input())
    a = 0
    while c > 1:
        a += 1
        c *= 1/2
    print(a, 'dias')
        
