sumlist=[]
while True:
    a,b=map(int, input().split())
    if a==0 and b==0:
        break
    i=0
    sumlist.append(a+b)
    i+=1

for c in sumlist:
    print(c)
