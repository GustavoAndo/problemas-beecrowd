rf = []
n = int(input())
for i in range(n):
    v = int(input())
    r = ''
    if v == 0:
        r += 'NULL'
    else:    
        if v%2 == 0: r += 'EVEN '
        else: r += 'ODD '
        if v > 0: r += 'POSITIVE'
        else: r += 'NEGATIVE'
    rf.append(r)    
for i in rf:
    print(i)
