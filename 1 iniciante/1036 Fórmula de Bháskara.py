v = input().split(' ')
a, b, c = float(v[0]), float(v[1]), float(v[2])
delta = b**2-4*a*c
if delta < 0 or a == 0:
    print('Impossivel calcular')
else:
    print(f'R1 = {(-b+(delta)**(1/2))/(2*a):.5f}')
    print(f'R2 = {(-b-(delta)**(1/2))/(2*a):.5f}')
