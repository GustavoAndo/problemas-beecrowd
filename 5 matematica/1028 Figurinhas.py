n = int(input())

for i in range(n):
    f = [int(i) for i in input().split()]
    f1, f2 = f[0], f[1]

    for i in range(min(f), 1, -1):
        if f1 % i == 0 and f2 % i == 0:
            print(i)
            break
