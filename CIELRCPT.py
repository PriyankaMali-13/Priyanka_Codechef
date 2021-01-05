lst = [1,2,4,8,16,32,64,128,256,512,1024,2048]
for _ in range(int(input())):
    k = int(input())
    count = 0
    
    while True:
        for i in range(len(lst)):
            if lst[i]<=k:
                small = lst[i]
        k=k-small
        count+=1
        if k == 0:
            break
    print(count)
    


        
