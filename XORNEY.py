from operator import xor 
def findXOR(n): 
    mod = n % 4 
    if (mod == 0): 
        return n 
    elif (mod == 1): 
        return 1 
    elif (mod == 2): 
        return n + 1 
    elif (mod == 3): 
        return 0 
def findXORFun(l, r): 
    res=(xor(findXOR(l - 1) , findXOR(r))) 
    return res
for _ in range(int(input())):
    l,r = map(int, input().split())
    if findXORFun(l,r) % 2==0:
        print('Even')
    else:
        print('Odd')
