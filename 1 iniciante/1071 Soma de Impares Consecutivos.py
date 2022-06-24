x = int(input())
y = int(input())
v = [x, y]
v.sort()
soma = 0
n = 0
if v[0] > 0 or v[0] % 2 == 1: n = 1
for i in range(v[0]+n, v[1]):
    if i % 2 == 1: soma += i
print(soma)
