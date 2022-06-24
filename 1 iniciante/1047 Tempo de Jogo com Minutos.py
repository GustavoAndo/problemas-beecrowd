hi, mi, hf, mf = (int(i) for i in input().split(' '))

if hf < hi: ht = hf - hi + 24
else: ht = hf - hi

if mf < mi:
    mt = mf - mi + 60
    if ht == 0: ht = 23
    else: ht -= 1
else:
    mt = mf - mi
    
if hf == hi and mi == mf: ht = 24

print('O JOGO DUROU', ht, 'HORA(S) E', mt, 'MINUTO(S)')
