for _ in range(int(input())):
    g = int(input())
    for p in range(g):
        i,n,q = map(int, input().split())
        if n%2 == 1:
            if i==q:
                print(n//2)
            else:
                print((n//2)+1)
        else:
            print(n//2)