v = input().split(' ')
a = int(v[0])
b = int(v[1])
c = int(v[2])
maior = (a + b + abs(a - b))/2
maior = (a + c + abs(a - c))/2 if maior == a else (b + c + abs(b - c))/2
print(int(maior), 'eh o maior')
