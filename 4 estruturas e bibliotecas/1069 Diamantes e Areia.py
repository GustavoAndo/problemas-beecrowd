q = int(input())

for i in range(q):  
    d = input().replace('.', '')
    cont = 0

    while True:
        if '<>' in d:
            d = d[:d.find('<>')] + d[d.find('<>')+2:]
            cont += 1
        else:
            break

    print(cont)
        
    
            
