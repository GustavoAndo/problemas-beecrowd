n = int(input())
cedulas = [100, 50, 20, 10, 5, 2, 1]
print(n)
for c in cedulas:
    print(f'{n//c} nota(s) de R$ {c},00')
    n = n%c
