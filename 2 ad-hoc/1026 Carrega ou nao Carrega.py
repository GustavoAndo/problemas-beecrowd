def binary(n):
    if n == 0: return 0
    r = ''
    while n != 0:
        r += str(n%2)
        n = n//2
    return r[::-1]

def decimal(n):
    s = 0
    n = str(n)
    for i in range(0, len(n)):
        s += 2**i*int(n[-i-1])
    return s

e = input().split(' ')
n1, n2, b, r = int(e[0]), int(e[1]), 0, ''
b1 = binary(n1)
b2 = binary(n2)
menor = b1 if int(b1) < int(b2) else b2
maior = b1 if int(b1) > int(b2) else b2
r = maior[:len(maior)-len(menor)]
maior = maior[len(maior)-len(menor):]
for i in range(0, len(menor)):
    if int(maior[i]) + int(menor[i]) == 1: r += '1'
    else: r += '0'
print(decimal(int(r)))
