def FindOptimal(l):
    l.sort()
    x=min(l)
    y=l[1]
    z=max(l)
    sum=abs(x-y)+abs(y-z)+abs(z-x)
    return sum

for _ in range(int(input())):
    n = int(input())
    l = list(map(int, input().split()))
    print(FindOptimal(l))