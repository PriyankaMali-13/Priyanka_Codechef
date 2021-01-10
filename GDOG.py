for _ in range(int(input())):
    l=[]
    n,k = map(int, input().split())
    for i in range(k+1):
        l.append(k%i)
    print(max(l))
