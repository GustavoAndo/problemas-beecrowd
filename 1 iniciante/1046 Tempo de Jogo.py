v = input().split(' ')
a, b = int(v[0]), int(v[1])
if a > b: h = 24 - a + b
elif b > a: h = b - a
else: h = 24
print(f'O JOGO DUROU {h} HORA(S)')
