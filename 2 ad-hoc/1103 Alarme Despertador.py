while True:
    h1, m1, h2, m2 = (int(i) for i in input().split())

    if h1 == m1 == h2 == m2 == 0: break

    if h2 >= h1: ht = h2 - h1
    else: ht = h2 - h1 + 24

    if m2 >= m1: mt = m2 - m1
    else:
        mt = m2 - m1 + 60
        if ht == 0: ht = 23
        else: ht -= 1
    
    print(ht*60+mt)
    


    
