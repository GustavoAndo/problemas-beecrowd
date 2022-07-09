l = int(input())
t = input()
m = []

for i in range(12):
    lm = []
    for j in range(12):
        n = float(input())
        lm.append(n)
    m.append(lm)
    
s = 0    
for i in range(12):
    s += m[l][i]
    
if t == 'M':
    s /= 12

print('%.1f'%s)
