a = float(input())
b = float(input())
c = float(input())
d = float(input())
e = float(input())
f = float(input())
v = [a, b, c, d, e, f]
r = []
for i in v:
    if i > 0: r.append(i)
print(len(r), 'valores positivos')
print(sum(r)/len(r))
