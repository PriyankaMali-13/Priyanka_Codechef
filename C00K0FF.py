for _ in range(int(input())):
    n = int(input())
    l = [0,0,0,0,0]
    for i in range(n):
        val = input()
        if val == 'cakewalk':
            l[0]+=1
        elif val == 'simple':
            l[1]+=1
        elif val == 'easy':
            l[2]+=1
        elif val == 'easy-medium' or val == 'medium':
            l[3]+=1
        elif val == 'medium-hard' or val == 'hard':
            l[4]+=1
    if 0 in l :
        print('No')
    else:
        print('Yes')

    

    

    
    
    
    
   
    
    