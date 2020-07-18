def minimumAbsoluteDifference(a,n):
    a.sort()

    m = 1000000000000000000

    for i in range(0,n-1):
        l = abs(a[i+1]-a[i])

        if l<m:
            m=l
    return m
    









n = int(input())

a = list(map(int,input().split(" ")))
print(a)

print(get_ans(a,len(a))

