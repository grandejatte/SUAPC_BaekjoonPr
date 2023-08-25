total=int(input())
jongryu=int(input())
i=0
tprice=0
while i<jongryu:
    price, many=map(int,input().split())
    i+=1
    tprice+=price*many

if tprice==total:
    print('Yes')
else:
    print('No')


