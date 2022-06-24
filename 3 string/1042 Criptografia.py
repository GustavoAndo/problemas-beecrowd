q = int(input())

for i in range(q):
    msg = input()  
    crip = ''
    cont = 0
    
    for i in msg[::-1]:
        if cont >= len(msg)//2:
            if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90):
                crip += chr(ord(i)+2)             
            else:
                crip += chr(ord(i)-1)
        else:
            if (ord(i) >= 97 and ord(i) <= 122) or (ord(i) >= 65 and ord(i) <= 90):
                crip += chr(ord(i)+3)
            else:
                crip += i              
        cont += 1
                
    print(crip)
