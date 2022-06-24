while True:
    m, n = (int(i) for i in input().split())
    if m <= 0 or n <= 0: break
    soma = 0
    if m > n:
        ini = n
        fim = m
    else:
        ini = m
        fim = n
    for i in range(ini, fim+1):
        print(i, end=' ')
        soma += i
    print('Sum={0}'.format(soma))
    
