def bubble_sort(a):
    n = len(a)
    swap = 0

    for i in range(0,n):
        for j in range(0,n-1):
            if a[j]>a[j+1]:
                temp = a[j]
                a[j] = a[j+1]
                a[j+1] = temp
                swap+=1
    return a

a = list(map(int,input().split(" ")))
print(bubble_sort(a))