def div(num):
    l = []
    for i in range(1,11):
        if num%i==0:
            l.append(i)
    return max(l)

n = int(input())
print(div(n))