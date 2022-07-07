q = int(input())
dic = {}
for i in range(q):
    n = int(input())
    if n not in dic: dic[n] = 1
    else: dic[n] += 1
for i in sorted(dic):
    print(i, 'aparece', dic[i], 'vez(es)')
    
