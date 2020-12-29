for _ in range(int(input())):
    n = int(input())
    a = list(map(int, input().split()))
    curr_max = float('inf')
    count = 0
    for i in range(len(a)):
        if a[i] <= curr_max:
            curr_max=a[i]
            count +=1
    print(count)

