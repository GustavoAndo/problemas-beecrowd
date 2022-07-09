n = int(input())
for i in range(n):
    x, y = (int(i) for i in input().split())
    try:
        print(x/y)
    except:
        print('divisao impossivel')
