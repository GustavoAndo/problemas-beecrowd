v = input().split(' ')
a, b, c = float(v[0]), float(v[1]), float(v[2])
print(f'PERIMETRO = {a+b+c:.1f}') if a < b + c and b < a + c and c < a + b else print(f'AREA = {(a+b)*c/2}')
