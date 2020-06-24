from collections import Counter
import math
r = int(input())
arr = list(map(int,input().split(" ")))
left_dict  = {}
right_dict = Counter(arr)
for_r_1 = right_dict
n  = len(arr)

#print("..........")

'''
print(left_dict)
print(right_dict)
'''
def NCR(n,r):
    return math.factorial(n)/(math.factorial(n-r)*math.factorial(r))

ans  = 0
if r!=1:
    for i in range(0,n-1):
        print(".............")
        print(i)
        left_count = 0
        right_count = 0
        a = arr[i]
        ar = int(a*r)
        a_ = a//r
        print(a_,a,ar)
        try:
            left_dict[a]+=1
        except:
            left_dict[a]=1
        right_dict[a]-=1
        try:
            if left_dict[a]!=-2:
                #print(a)
                left_count = left_dict[a_]
        except:
            left_count = 0
        try:
            if right_dict[ar]!=-1:
                #print(ar)
                right_count = right_dict[ar]
        except:
            pass


        ans = ans + ( left_count*right_count )
        print(left_count,right_count)
        #print(left_dict)
        #print(right_dict)
else:
    for i in for_r_1:
        ans = ans + NCR(for_r_1[i],3)

print(int(ans))





        












