for _ in range(int(input())):
    n,k = map(int, input().split())
    a = list(map(int, input().split()))
    c = []
    for i in range(len(a)):
        if a[i]<=k:
            k-=a[i]
            c.append(1)
        else:
            c.append(0)
    print(*c,sep='')