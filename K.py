from fractions import Fraction
i=0
flistx=[]
flisty=[]
while i<4:
    x,y=map(int,input().split())
    flistx.append(x)
    flisty.append(y)
    i+=1
    
k=0
slistx=[]
slisty=[]
while k<4:
    a,b=map(int,input().split())
    slistx.append(a)
    slisty.append(b)
    k+=1

flistx.sort()
flisty.sort()
slistx.sort()
slisty.sort()
print(flistx,flisty)
print(slistx,slisty)

fm_x=(flistx[0]+flistx[3])/2
fm_y=(flisty[0]+flisty[3])/2
sm_x=(slistx[0]+slistx[3])/2
sm_y=(slisty[0]+slisty[3])/2

print(fm_x,fm_y,sm_x,sm_y)

p=(sm_y-fm_y)/(sm_x-fm_x)
q=fm_y-p*fm_x
p=Fraction.from_float(p)
q=Fraction.from_float(q)

print(p,q)
