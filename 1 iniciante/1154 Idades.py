t = []
while True:
    i = int(input())
    if i < 0: break
    t.append(i)
m = sum(t)/len(t)
print('%.2f'%m)
    
