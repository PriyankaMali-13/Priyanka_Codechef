for _ in range(int(input())):
    s1 = input()
    s2 = input()
    if len(s1)==len(s2):
        c = 0
        for i in range(len(s1)):
            if s1[i]!=s2[i] and s1[i]!='?' and s2[i]!='?':
                c = 0
                break
            else:
                c = 1
    if c==1:
        print('Yes')
    else:
        print('No')
        
    