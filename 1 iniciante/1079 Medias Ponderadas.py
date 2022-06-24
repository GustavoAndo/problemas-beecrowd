q = int(input())
for i in range(q):
    ns = input().split()
    n1, n2, n3 = float(ns[0]), float(ns[1]), float(ns[2])
    print(f'{(n1*2+n2*3+n3*5)/10:.1f}')
