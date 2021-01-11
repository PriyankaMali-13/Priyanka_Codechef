for _ in range(int(input())):
    a = input()
    b = input()
    if len(a)==len(b):
        max = 0
        min = 0
        for i in range(len(a)):
            if a[i]!=b[i] and a[i]!='?' and b[i]!='?':
                min+=1
            if a[i]!=b[i] or a[i]=='?' or b[i]=='?':
                max+=1
    print(min,max)