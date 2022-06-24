v = input().split(' ')
A, B, C, D = int(v[0]), int(v[1]), int(v[2]), int(v[3])
print('Valores aceitos') if B > C and D > A and C + D > A + B and C > 0 and D > 0 and A % 2 == 0 else print('Valores nao aceitos')
