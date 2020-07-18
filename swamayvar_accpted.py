n=int(input())
w=list(input())
m=list(input())
f=0
c=0
while(len(w)>0 and len(m)>0 and f!=1 ):
    if w[0]==m[0]:
        w.remove(w[0])
        m.remove(m[0])
        c=0
    else:
        temp=m[0]
        m.remove(m[0])
        m.append(temp)
        c=c+1
    if c==len(m):
        f=1
        break
print(len(m),end='')