v = float(input())
cedulas = [100, 50, 20, 10, 5, 2]
moedas = [100, 50, 25, 10, 5, 1]
print('NOTAS:')
for c in cedulas:
    print(f'{int(v//c)} nota(s) de R$ {c:.2f}')
    v %= c
print('MOEDAS:')
v *= 100
for m in moedas:   
    print(f'{int(v//m)} moeda(s) de R$ {m/100:.2f}')
    v %= m
