import bisect
def med(arr,d,m):
    if d%2==0:
        a  = sum(arr[m-1:m+1])/2
        return a
    else:
        return arr[m] 

d = int(input())
arr = list(map(int,input().split(" ")))
n = len(arr)
#print(statistics.median(arr))
temp = sorted(arr[0:d])
#print(temp)
m = d//2
count = 0



for i in range(d,n):
    if arr[d]>=2*med(temp,d,m):
        count += 1

    del temp[bisect.bisect_left(temp,arr[i-d])]
    bisect.insort(temp,arr[i])

print(count)







