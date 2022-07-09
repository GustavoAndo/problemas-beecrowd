while True:
    try:
        e = input()
        ps = ''
        for l in e:
            if l == '(' or l == ')':
                ps += l
                
        v = [] 
        for p in ps:
            if p == ')' and len(v) != 0:
                if v[-1] == '(': v.pop()
                else:
                   print('incorrect')
                   break
            else: v.append(p)

        if len(v) == 0: print('correct')
        else: print('incorrect')
    except EOFError:
        break
    

