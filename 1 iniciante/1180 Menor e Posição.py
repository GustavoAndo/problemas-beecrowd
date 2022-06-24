n = int(input())
v = [int(i) for i in input().split()]
print('Menor valor:', min(v))
print('Posicao:', v.index(min(v)))
