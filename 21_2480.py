import random

x,y,z=map(int, input().split())
mlist=[x,y,z]

if x==y and x!=z:
    p=1000+x*100
elif y==z and y!=x:
    p=1000+y*100
elif z==x and z!=y:
    p=1000+x*100
elif x==y and y==z:
    p=10000+x*1000
elif x!=y and y!=z and z!=x:
    p=int(max(mlist))*100

print(p)
