def get_ans(a,k):
    imp = []
    non_imp = []
    luck = 0

    for i in range(0,len(a)):
        if a[i][1]==1:
            imp.append(a[i][0])
        else:
            non_imp.append(a[i][0])
    imp.sort(reverse = True)
    
    for i in range(0,len(imp)):
        
        if i<=(k-1):
            luck += imp[i]
        else:
            luck -= imp[i]

    luck += sum(non_imp)

    print(luck)



n,k = map(int,input().split(" "))
aa = []
for i in range(0,n):
    m,y=map(int,input().split(" "))
    aa.append([m,y])
print(aa)

get_ans(aa,k)



    


