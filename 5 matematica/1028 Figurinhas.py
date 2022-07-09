n = int(input())

for i in range(n):
    f = [int(i) for i in input().split()]
    f1, f2 = min(f), max(f)

    while True:
        if f1%f2 == 0: break
        f1, f2 = f2, f1%f2
        
    print(f2)
