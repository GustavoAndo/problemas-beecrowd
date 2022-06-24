v = [int(input())]
for i in range(10):
    print(f'N[{i}] = {v[i]}')
    v.append(v[i]*2)
