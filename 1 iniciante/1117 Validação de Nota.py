ns = []
while True:
    if len(ns) == 2: break
    n = float(input())
    if n <= 10 and n >= 0: ns.append(n)
    else: print('nota invalida')
m = sum(ns)/2
print('media =', '%.2f' % m)
