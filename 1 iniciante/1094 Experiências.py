n = int(input())
c, r, s, tot = 0, 0, 0, 0
for i in range(n):
    q, t = input().split()
    q = int(q)
    if t == 'C':  c += q
    elif t == 'R': r += q
    else: s += q
    tot += q
    
print('Total:', tot, 'cobaias')
print('Total de coelhos:', c)
print('Total de ratos:', r)
print('Total de sapos:', s)

pc = c*100/tot
pr = r*100/tot
ps = s*100/tot

print('Percentual de coelhos:', '%.2f'%pc, '%')
print('Percentual de ratos:', '%.2f'%pr, '%')
print('Percentual de sapos:', '%.2f'%ps, '%')
