for _ in range(int(input())):
    n, ans = map(int, input().split())
    a = list(map(int, input().split()))
    for i in range(len(a)):
        ans = ans-a[i]
    if ans<0:
        print('No')
    else:
        print('Yes')
