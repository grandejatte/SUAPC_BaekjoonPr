n=int(input('1: '))
hlist=[]
hlist.append('')
i=0
while i<n:
    i+=1
    hlist[i]=input()

nn=input('3: ')

print(hlist.count(nn))
