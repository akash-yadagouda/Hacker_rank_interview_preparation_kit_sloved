def get_ans(arr,k,n):

    arr.sort(reverse = True)

    c = 0
    price = 0
    lasti = 0
    lastc = 0
    i = 0

    while i<n:
        j = 0
        c+=1
        while j<k and (i+j)<n:
            price = price + arr[i+j]*(c)
            lasti = (i+j)
            lastc = c
            #print(i+j)
            j += 1 
        i = i + k

    #print(price)
    return price


n, k = map(int,input().split(" "))
arr = list(map(int,input().split(" ")))
print(get_ans(arr,k,n))



