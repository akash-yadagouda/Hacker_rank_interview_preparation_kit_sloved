



from collections import Counter
import math


def NCR(n,r):
    return math.factorial(n)/(math.factorial(n-r)*math.factorial(r))

'''
print(NCR(100000,3))
'''

k = list(map(int,input().split(" ")))
arr = []
r = 2
for i in k:
    if i%r==0 or i==1:
        arr.append(i)


d = (Counter(sorted(arr)))
li = sorted(d)
d = sorted(d.items())
d = dict(d)
print(d)
print(li)
co = 1
ans = 0
ak = len(li)
if r==1:
    i = 0
    while ak>0:
        if d[li[i]]>2:
            ans = ans + int(NCR(d[li[0]],3))
        ak = ak -1
else:
    for i in range(0,len(li)-2):
        if li[i+2]//li[i+1]==r:
            if li[i+1]//li[i]==r:
                ans = ans + int(d[li[i]]*d[li[i+1]]*d[li[i+2]])

print(ans)
    





