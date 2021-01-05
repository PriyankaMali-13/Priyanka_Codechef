w, amount = map(float, input().split())
if w%5==0 and w+0.50<amount:
    a=(amount-w)-0.50
    print('%.2f'% a)
else:
    print('%.2f'% amount)



