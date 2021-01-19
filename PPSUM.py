for _ in range(int(input())):
    d,n = map(int, input().split())
    sum = n
    while d>0:
        for i in range(sum):
            sum+=i
        d-=1
    print(sum)