for _ in range(int(input())):
    num1,num2 = map(int, input().split())
    if num1>num2:
        n = num1
        d = num2
    else:
        n = num2
        d = num1
    r = n%d
    while r!=0:
        n=d
        d=r
        r = n%d
    gcd = d
    lcm = (num1*num2)//gcd
    print(gcd,lcm)
