def find_gcd(x,y):
    while y:
        x,y = y,x%y
    return x
for _ in range(int(input())):
    l = list(map(int, input().split()))
    ans = []
    num1 = l[1]
    num2 = l[2]
    gcd = find_gcd(num1,num2)
    for i in range(1,len(l)):
        gcd = find_gcd(gcd,l[i])
    for j in range(1,len(l)):
        ans.append(l[j]//gcd)
    print(*ans)


    
    
    
    