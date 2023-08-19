h,m=map(int,input().split())
c=int(input())

if m+c>=60:
    x=int(((m+c)-((m+c)%60))/60)
    h+=x
    m=(m+c)-60*x
    if h>=24:
        h-=24

elif m+c<60:
    m+=c

print(h,m)
