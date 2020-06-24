size = int(input())
dic = []

a = 0
b = 0

for i in range(0,size):
    a = list(map(int,input().split(" ")))
    dic.append(a)
#print(dic)

dd = {}
ans = []

for i in range(0,size):
    if dic[i][0]==1:
        try:
            #print("in try")
            if dd[dic[i][1]]!=0:
                dd[dic[i][1]]+=1
        except:
            #print("in except")
            dd[dic[i][1]]=1
    if dic[i][0]==2:
        #print("if 2")
        try:
            if dd[dic[i][1]]>0:
                dd[dic[i][1]]-=1
        except:
            pass
    if dic[i][0]==3:
        key = list(dd.keys())
        value = list(dd.values())
        #print(key)
        #print(value)
        try:
            q=value.index(dic[i][1])
            print(1)
            ans.append(1)
        except:
            print(0)
            ans.append(0)



#print(dd)
