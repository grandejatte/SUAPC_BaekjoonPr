H, M=map(int,input().split())
while not 0<=H<=23:
    H, M=map(int,input().split())
while not 0<=M<=59:
    H, M=map(int,input().split())
    
if H != 0:
    if M>45:
        M-=45
    elif M==45:
        M=0
    else:
        H-=1
        M=60-(45-M)

else:
    H=23
    M=60-(45-M)
    
print(H, M)
