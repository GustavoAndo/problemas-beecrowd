n = int(input())
v = []
while True:
    for i in range(n): v.append(i)
    if len(v) >= 1000: break
while len(v) > 1000: v.pop()
for i in range(len(v)): print('N['+ str(i) +'] = ' + str(v[i]))
