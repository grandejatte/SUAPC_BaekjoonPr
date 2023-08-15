x=int(input())
y=int(input())

if x>0:
    if y>0:
        n=1
    if y<0:
        n=4
if x<0:
    if y>0:
        n=2
    if y<0:
        n=3

print(n)
