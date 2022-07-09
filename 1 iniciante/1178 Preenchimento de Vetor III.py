x = float(input())
n = [x]
for i in range(99):
    x /= 2
    n.append(x)
for i in range(100):
    print('N[' + str(i) + '] = ' + '%.4f'%n[i])
