a = input().split(' ')
b = input().split(' ')
from math import sqrt
print(f'{sqrt((float(b[0]) - float(a[0]))**2+(float(b[1]) - float(a[1]))**2):.4f}')
