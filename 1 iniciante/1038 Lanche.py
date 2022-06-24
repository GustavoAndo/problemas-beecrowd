e = input().split(' ')
c, q, t = int(e[0]), int(e[1]), 0
if c == 1: t = q*4.00
elif c == 2: t = q*4.50
elif c == 3: t = q*5.00
elif c == 4: t = q*2.00
else: t = q*1.00
print(f'Total: R$ {t:.2f}')
