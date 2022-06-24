def fat(n):
    if n == 0 or n == 1: return 1
    return n*fat(n-1)

while True:
    try:
        n, m = (int(i) for i in input().split())
        print(fat(n)+fat(m)) 
    except EOFError:
        break
