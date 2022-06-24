a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
v = [a, b, c, d, e]
contpar, conti, contp, contn = 0, 0, 0, 0
for i in v:
    if i%2 == 0: contpar += 1
    else: conti += 1
    if i > 0: contp += 1
    if i < 0: contn += 1
print(f'{contpar} valor(es) par(es)')
print(f'{conti} valor(es) impar(es)')
print(f'{contp} valor(es) positivo(s)')
print(f'{contn} valor(es) negativo(s)')
