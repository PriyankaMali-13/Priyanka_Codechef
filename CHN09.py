for _ in range(int(input())):
    s = input()
    c_a = 0
    c_b = 0
    for i in range(len(s)):
        if s[i]=='a':
            c_a+=1
        elif s[i]=='b':
            c_b+=1
    if c_a == c_b:
        print(c_a)
    else:
        print(min(c_a,c_b))
    
    
    