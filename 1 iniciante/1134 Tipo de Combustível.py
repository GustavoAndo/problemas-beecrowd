a, g, d = 0, 0, 0

while True:
    comb = input()
    if comb == '1': a += 1
    elif comb == '2': g += 1
    elif comb == '3': d += 1
    elif comb == '4': break

print('MUITO OBRIGADO')
print('Alcool:', a)
print('Gasolina:', g)
print('Diesel:', d)
