a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
v = [a, b, c, d, e, f]
cont = 0
for i in v:
    if i > 0: cont += 1
print(cont, 'valores positivos')
