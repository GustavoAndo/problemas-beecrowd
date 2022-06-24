a = []
for i in range(100):
    n = float(input())
    a.append(n)
for i in range(len(a)):
    if a[i] <= 10:
        print('A[{0}] = '.format(i), end='')
        print('%.1f'%a[i])
