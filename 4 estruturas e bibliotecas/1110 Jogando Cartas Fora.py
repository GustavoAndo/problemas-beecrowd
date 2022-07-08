while True:
    n = int(input())
    if n == 0: break
    cs = []
    for i in range(1, n+1):
        cs.append(i)
    print('Discarded cards:' ,end=' ')
    while len(cs) > 1:
        if len(cs) > 2: print(cs.pop(0), end=', ')
        else: print(cs.pop(0))
        cs.append(cs.pop(0))
    print('Remaining card:', cs[0])


    
