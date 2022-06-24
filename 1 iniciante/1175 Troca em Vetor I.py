r = []
for i in range(20):
    n = int(input())
    r.append(n)
r.reverse()
for j in range(len(r)):
    print(f'N[{j}] = {r[j]}')
