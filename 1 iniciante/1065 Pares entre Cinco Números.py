a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
v, cont = [a, b, c, d, e], 0
for i in v:
    if i%2 == 0: cont += 1
print(cont, 'valores pares')
