for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    a[a.index(max(a))]=0
    b[b.index(max(b))]=0
    if sum(a) == sum(b):
        print('Draw')
    elif sum(a) < sum(b):
        print('Alice')
    else:
        print('Bob')
    
    
   
    
    