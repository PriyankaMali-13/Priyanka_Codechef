for _ in range(int(input())):
    n = int(input())
    d = {'1':0, '2':0, '5':0, '10':0, '50':0, '100':0}
    add = 0
    while n>0:
        if n>=100:
            n-=100
            d['100']+=1
        elif n<100 and n>=50:
            n-=50
            d['50']+=1
        elif n<50 and n>=10:
            n-=10
            d['10']+=1
        elif n<10 and n>=5:
            n-=5
            d['5']+=1
        elif n<5 and n>=2:
            n-=2
            d['2']+=1
        else:
            n-=1
            d['1']+=1
        if n==0:
            break
    for i in d:
        add+=d[i]
    print(add)

