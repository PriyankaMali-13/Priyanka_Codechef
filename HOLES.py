for _ in range(int(input())):
    l = ['A','D','O','P','R','Q']
    s = input()
    count = 0
    for i in range(len(s)):
        if s[i] in l:
            count+=1
        elif s[i] == 'B':
            count+=2
    print(count)
