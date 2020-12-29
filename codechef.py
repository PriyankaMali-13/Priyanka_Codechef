#Easy math problem
t = int(input())
product = 1

add = 0
for _ in range(t) :
    n = int(input())
    for i in range(n) :
        a = map(int, input().split())
        for j in a :
            product *= j
        #li.append(product)
        #print(li)
        s = list(str(product))
        print(s)
        for l in s:
            add += int(l)
        print(add)


        

    