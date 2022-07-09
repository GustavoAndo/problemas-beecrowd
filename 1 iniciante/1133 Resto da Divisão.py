x = int(input())
y = int(input())
v = [x, y]
for i in range(min(v)+1,max(v)):
    if i%5 == 2 or i%5 == 3: print(i)
