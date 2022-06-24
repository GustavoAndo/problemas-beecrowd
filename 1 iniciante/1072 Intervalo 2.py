n = int(input())
contin, contout = 0, 0
for i in range(n):
    x = int(input())
    if 10 <= x <= 20: contin += 1
    else: contout += 1
print(contin, 'in')
print(contin, 'out')
