n = int(input())
for i in range(n):
    s = input()
    c = int(input())
    r = ''
    for i in s:
        v = ord(i) - c
        if v < 65: r += chr(v+26)
        else: r += chr(v)
    print(r)
        
