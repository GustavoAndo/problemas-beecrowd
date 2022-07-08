e = input()
e = [c for c in e if c =='(' or c == ')']
while True:
    if len(e) % 2 == 1:
        print('incorrect')
        break
    if len(e) == 0:
        print('correct')
        break
    if e[0] == '(':
        if ')' not in e:
            print('incorrect')
            break
        for i in range(1, len(e)):
            if e[i] == ')':
                e.pop(i)
                e.pop(0)
                break
    else:
        print('incorrect')
        break

